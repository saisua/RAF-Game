from random import choice, randint
from collections import defaultdict
from time import sleep
from termcolor import colored
import datetime

from Combatter import Combatter

from Conditions.Stages.Dojo import Dojo
from Conditions.Stages.Forest import Forest
from Conditions.Stages.House import House
from Conditions.Stages.Planes import Planes

from Conditions.Climates.Climate import Climate as Default_climate
from Conditions.Climates.Hail import Hail
from Conditions.Climates.Rainy import Rainy
from Conditions.Climates.Sunny import Sunny

from Items.Armors.Random_armor import armor_types

class Combat():
    PRINTING_WAIT = 1.8

    stage:"Stage"
    climate:"Climate"

    CHANCE_NOT_ALLOWED:int = 50
    MAX_HELD_ITEMS:int = 1
    MAX_EQUIPED_ARMOR:int = armor_types
    MAX_HITS_TURN:int = 3
    MAX_PETS_FRONT:int = 1
    MAX_PETS_BACK:int = 3

    XP_PLAYER:int = 5

    rule_names:list = ["Armor", "Pet", "Spell", "Weapon", "reusing weapons", "Ability"]
    rules:dict

    active_rules:bool=False

    participants = defaultdict(list)
    starting_participants:set
    str_edited:bool = True
    last_str:str

    attack_order:list

    def __init__(self, teams:dict={}, *, disable_rules:bool=False):
        self.stage = choice([Dojo, Forest, House, Planes])()

        if(not self.stage.inside):
            self.climate = choice([Hail, Rainy, Sunny])()
        else:
            self.climate = Default_climate()

        self.rules = {}

        if(not disable_rules):
            for rule in self.rule_names:
                self.rules[rule] = bool(randint(0,self.CHANCE_NOT_ALLOWED))

            self.active_rules = not all(self.rules.values())

        self.participants = dict({team_name:[Combatter(self, participant, team_num, team_name) 
                                for participant in team]
                                for team_num, (team_name, team) in enumerate(teams.items())})
        self.starting_participants = {participant for participants in self.participants.values() for participant in participants}

        for participant in self.starting_participants:
            if(not participant.character._can_play):
                print(f"\n\n{participant} cannot play any more combats today")
                exit(0)

    def __str__(self):
        if(not self.str_edited):
            return last_str

        result = f"A combat in a {self.stage.name}"

        if(not self.stage.inside):
            result += f" on a {self.climate.name} day!"

        if(self.active_rules):
            result += "\n\n### RULES ###\n\n"

            for rule, allowed in self.rules.items():
                if(not allowed):
                    result += colored(f"  - No {rule} allowed\n", "yellow")
            

        result += "\n\nPARTICIPANTS\n"

        if(len(self.participants)):
            for team, members in self.participants.items():
                result += f"\n # TEAM {team} #\n"

                for member in members:
                    result += f"  - {member.name}\n"
        else:
            result += "  No participants yet\n"

        self.str_edited = False
        self.last_str = result

        return result

    def start(self):
        print(" ### STARTING A COMBAT ###\n\n"+self.__str__())
        self.attack_order = []
        #movement_order = []

        for team in self.participants.values():
            self.attack_order.extend(team) 
        #movement_order = sorted([*team for team in self.participants.items()], 
        #        key=lambda char: char.attributes.speed)

        self.attack_order.sort(key=lambda char: char.attributes.attack_speed)
        #movement_order.sort(key=lambda char: char.attributes.speed)
        

        attack_num = 0
        #movement_num = 0

        sleep(self.PRINTING_WAIT*3)

        turn_cycle = 0

        while(len(self.participants) > 1):
            attacker_turn = self.attack_order.pop(0)
            #move_turn, turns2 = movement_order.pop(0)

            if(not attacker_turn.is_alive):
                continue

            attacker_turn.turn += 1
            #turns2 += 1

            if(attacker_turn.cannot_attack_turns <= 0):

                num_attacks = attacker_turn.attacks_per_turn if randint(0,15) else randint(1, self.MAX_HITS_TURN)

                print(f"It's [{attacker_turn.team_name}] {attacker_turn.name}'s turn to attack. ",end='')

                if(num_attacks > 1):
                    print(f"Attacks {num_attacks} times!")
                else:
                    print()

                for _ in range(num_attacks):
                    self.attack(attacker_turn, is_companion=attacker_turn.is_companion)
                    print("++++")

                    if(len(self.participants) <= 1): break
                else:
                    print()
            else:
                print(f"[{attacker_turn.team_name}] {attacker_turn.name} can't attack because {attacker_turn.cannot_attack}\n++++\n")
                attacker_turn.cannot_attack_turns -= 1

                if(attacker_turn.cannot_attack_turns <= 0):
                    attacker_turn.cannot_attack = ''
                    attacker_turn.cannot_attack_turns = 0

            if(not attacker_turn in self.attack_order):
                for num, attacker in enumerate(self.attack_order):
                    if(attacker_turn.attributes.attack_speed*attacker.turn > 
                                attacker.attributes.attack_speed*attacker_turn.turn):
                        self.attack_order.insert(num, attacker_turn)
                        break
                else:
                    self.attack_order.append(attacker_turn)

            if(turn_cycle >= sum([len(m) for m in self.participants.values()])):
                turn_cycle = 0

                print("~~~~")
                for team in self.participants.values():
                    for member in team:
                        if(len(member.effects)):
                            member.apply_effects()
                            print("~~~")
                print()
                sleep(self.PRINTING_WAIT)

            turn_cycle += 1

            sleep(self.PRINTING_WAIT)

        winner_team, winner_list = list(self.participants.items())[0]

        print(f"\n\n\n  #### THE COMBAT HAS ENDED! ####\n\n The winner is team {winner_team}!\n")
        print("Alive members:")
        for member in self.participants[winner_team]:
            print(f"  - {member}    hp: {member.life}")
            for pet_list in member.pets.values():
                for pet in pet_list:
                    print(f"    - {pet}    hp: {pet._life}")

        print("\nCongratulations!\n")

        received_xp = set()

        now = datetime.datetime.now()

        for participant in winner_list+list(self.starting_participants):
            if(participant._static in received_xp):
                continue

            xp = self.XP_PLAYER*(
                        len(self.starting_participants)
                        )*(2 if participant.team_name == winner_team else 1)
            if(participant in winner_list):
                xp = int(xp*1.5)

            participant._static.get_xp(xp+randint(0,xp//self.XP_PLAYER))
            participant._static.end_combat(now)
            received_xp.add(participant._static)
            print()

        for participant in self.starting_participants:
            del participant

    def add_participant(self, new_participant:"Character", team:str=None):
        if(not new_participant._can_play):
            print(f"\n\n{new_participant} cannot play any more combats today")
            exit(0)

        if(team is None):
            team = str(len(self.participants)+1)
            team_index = len(self.participants)
        else:
            if(team in self.participants):
                team_index = list(self.participants.keys()).index(team)
            else:
                team_index = len(self.participants)

        combatter = Combatter(self, new_participant, team_index, team)

        self.participants[team].append(combatter)
        self.starting_participants.add(combatter)
        
    def add_team(self, new_team:list, team:str=None):
        for participant in self.new_team:
            if(not participant._can_play):
                print(f"\n\n{participant} cannot play any more combats today")
                exit(0)

        if(team is None):
            team = str(len(self.participants)+1)
            team_index = len(self.participants)
        elif(team in self.participants):
            return False

        combatters = [Combatter(self, participant, team_index, team) for participant in new_team]

        self.participants[team].extend(combatters)
        self.starting_participants.update(set(combatters))

    def attack(self, character:Combatter, is_companion:bool=False):
        team = randint(0, len(self.participants)-2)

        character.attack(choice(list(self.participants.values())[
                team+(1 if team >= character.team_index else 0)]),
                can_call=any(self.rules))

    def move(self, character:Combatter):
        pass
