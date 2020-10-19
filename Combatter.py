from random import randint,choice
from collections import defaultdict
from termcolor import colored
from copy import deepcopy

from Items.Armors.Helmet import Helmet

HEAD_DAMAGE = Helmet.DAMAGE_PART

class Combatter():
    combat:"Combat"
    character:"Character"
    turn:int=0

    attributes:"Attributes"

    team_name:str
    team_index:int
    name:str

    callables:list = ["Pet", "Weapon", "Ability"]
    attacks:list = ["Spell"]

    effects:list

    max_held_items:int = 0
    held_items:list = []
    max_equiped_armor:int = 0
    equiped_armor:dict = {}
    max_pets_front:int = 0
    max_pets_back:int = 0
    max_pets_dict:dict = {"front": max_pets_front, "back": max_pets_back}
    pets:list = {"back":[], "front":[]}
    called_items:list = []

    is_companion:bool = False
    is_alive:bool = True
    cannot_attack:str = ''
    cannot_attack_turns:int = 0
    attacks_per_turn:int=1

    life_colors = ["red", "yellow", "green", "green"]
    magic_colors = ["blue", "cyan"]

    def __init__(self, combat:"Combat", character:"Character", team_index:int, team_name:str,
                    is_companion:bool=False):
        self.combat = combat
        self.character = character

        self.name = character.name
        self.team_name = team_name
        self.team_index = team_index

        self.effects = []

        if(not is_companion):
            self.callables = [c for c in self.callables if combat.rules[c]]
            self.attacks = [c for c in self.attacks if combat.rules[c]]

            self.max_held_items = min(self.character.max_held_items, self.combat.MAX_HELD_ITEMS)
            self.held_items = []
            # Can companions have armor?
            self.max_equiped_armor = min(self.character.max_equiped_armor, self.combat.MAX_EQUIPED_ARMOR)
            self.equiped_armor = {}

            self.pets = {"back":[], "front":[]}
            self.called_items = []

            self.max_pets_back = min(self.character.max_pets_back, self.combat.MAX_PETS_BACK)
            self.max_pets_front = min(self.character.max_pets_front, self.combat.MAX_PETS_FRONT)

            self.max_pets_dict:dict={"front": self.max_pets_front, "back": self.max_pets_back}

            # ADD ARMORS
            if(combat.rules["Armor"]):
                for armor_type, armor_list in character.items["Armor"].items():
                    if(len(armor_list)):
                        self.equiped_armor[armor_type] = choice(armor_list)

        self.attributes = deepcopy(character.attributes)

    def __str__(self):
        return self.character.__str__()

    def attack(self, enemy:"Combatter", *, can_call:bool=False):
        if(can_call and len(self.callables)):

            if(not bool(randint(0,5))):
                call_item = choice(self.callables)

                if(self.combat.rules[call_item] and len(self.character.items[call_item])):
                    new_item = choice(list(self.character.items[call_item].values()))

                    if(len(new_item) and randint(0,100) < self.attributes._get(call_item)):
                        choice(new_item).call(self, self.turn)

        special_attack = choice(self.attacks) if len(self.attacks) else None

        if(len(enemy.equiped_armor)):
            if(randint(0,100) < self.attributes.precission/2): # Crit attack
                attack_to = (None if len(enemy.equiped_armor) < self.combat.MAX_EQUIPED_ARMOR
                                else enemy.equiped_armor["Helmet"])
            else:
                attack_to = (choice(list(enemy.equiped_armor.values())) 
                        if randint(0, enemy.max_equiped_armor-1) < len(enemy.equiped_armor)
                        else None)
        else:
            attack_to = None

        if(self.combat.rules.get(special_attack, False) and randint(0,1) 
                    and len(self.character.items[special_attack])):
            spell = choice(list(self.character.items[special_attack].values()))

            if(len(spell)):
                spell = choice(spell)

                if(self.attributes.magic >= spell.magic):
                    if(not spell.attack(enemy, attack_to, self)):
                        print(f"{self.name} missed the spell!")
                    return
                    

        if(len(self.held_items)):
            for item in self.held_items:
                if(not enemy.is_alive): break

                if(randint(0,100) < self.attributes.precission and
                            randint(0,100) > enemy.attributes.evasion):
                    item.attack(enemy, attack_to, self)
                else:
                    print(f"{self.name} missed the attack!")
        else:
            if(randint(0,100) < self.attributes.precission and
                        randint(0,100) > enemy.attributes.evasion):
                print(f"{self.name} attacked {enemy.name} with bare hands!")
                enemy.receive_hit(self.attributes.strength, self, attack_to)
            else:
                print(f"{self.name} missed the attack!")

    def receive_hit(self, damage:int, attacker:"Combatter", attack_to:"Armor"=None, attack_form:str="melee"):
        if(len(self.pets["front"])):
            pet = self.pets["front"][0]
            print(f"{attacker.name} attacked [{self.team_name}] {self.name} but {pet.name} took the hit instead!")

            pet.receive_hit(damage, attacker, attack_form=attack_form)
        else:
            if(attack_form != "melee" and randint(0,len(self.pets["back"]))):
                pet = choice(self.pets["back"])

                pet.receive_hit(damage, attacker, attack_form=attack_form)
            else:
                damage = (damage-(self.attributes.defense if attack_form != "magic" else self.attributes.magic_defense))*(1+randint(0,10)/10)
                if(damage < 1): damage = 1

                if(attack_to):
                    print(f"[{self.team_name}] {self.name} received a hit on the {attack_to.name}! "
                            f"({self.life}hp -> ",end='')
                    after = attack_to.receive_hit(self, damage,attacker)
                    print(self.life, end='hp )\n')

                    print(after)
                else:
                    print(f"[{self.team_name}] {self.name} received a direct hit! "
                            f"({self.life}hp -> ",end='')

                    self.attributes.life -= damage*HEAD_DAMAGE

                    print(self.life, end='hp)\n')

                    if(randint(0,100) < attacker.attributes.stun):
                        self.add_cc(1, "stunned")

                    if(len(self.held_items) and randint(0,100) < attacker.attributes.knock):
                        dropped_weapon = self.held_items[randint(0, len(self.held_items)-1)]
                        dropped_weapon.drop(self, "because of the hit")

                if(self.attributes.life <= 0):
                    self.die()

    def add_effect(self, effect):
        self.effects.append(effect)
        effect.apply(self)

    def add_cc(self, turns:int, reason:str, after:str=''):
        if(not "is "+reason in self.cannot_attack):
            self.cannot_attack += f"{' and ' if self.cannot_attack else ''}is "+reason
        self.cannot_attack_turns += turns
        print(f"{self.name} also got {reason}{after}!")

    def move(self):
        raise NotImplementedError

    def die(self):
        print(f"\n## [{self.team_name}] {self.name} has fainted!\n\n")

        self.is_alive = False
        
        if(len(self.combat.participants[self.team_name]) > 1):
            self.combat.participants[self.team_name].remove(self)
        else:
            del self.combat.participants[self.team_name]

    def apply_effects(self):
        for effect in self.effects:
            effect.apply(self)

    # Auxiliar

    def add_pet(self, pet, position):
        if(position != "next"):
            if(len(self.pets[position]) < self.max_pets_dict[position] and 
                        not pet in self.pets[position]):
                self.pets[position].append(pet)
                return True
        else:
            if(not pet in self.combat.participants[self.team_name]):
                self.combat.participants[self.team_name].append(pet)
                return True


    def weakest_point(self):
        weakest = float('inf')
        for item in self.equiped_armor:
            weakest = min(weakest, item.protection)

        return weakest

    # Properties

    @property
    def life(self) -> str:
        color_index = int(self.attributes.life*(len(self.life_colors)-1)/(self.character.attributes.life+1))

        return colored(int(self.attributes.life), self.life_colors[0 if color_index < 0 else color_index])

    @property
    def magic(self) -> str:
        color_index = int(self.attributes.magic*(len(self.magic_colors)-1)/self.character.attributes.magic)

        return colored(int(self.attributes.magic), self.magic_colors[0 if color_index < 0 else color_index])

    @property
    def _static(self) -> "Character":
        return self.character