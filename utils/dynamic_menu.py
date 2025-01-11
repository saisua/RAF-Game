from os import get_terminal_size
from termcolor import colored
from typing import List, Callable, Union, Dict

class Menu():
    show_before:List[Union[str, Callable]]
    
    options:Dict[str, Callable]
    unselected_options:List[str]
    selected_options:List[str]
    __generated_columns:int=None

    selected_opt:int=0

    selected_str = "> "
    choose_str = ">> "
    borders:Dict[str,str] = {
        "UL":"⌜", 
        "Up":"-", 
        "UR":"⌝",
        "Left":"ǀ",
        "Right":"ǀ",
        "DL":"⌞",
        "Down":"-",
        "DR":"⌟"
    }
    max_columns:int = 2
    fill_before_menu:bool=False

    ter_size:int = get_terminal_size()

    __generated_menu:List[str]

    def __init__(self, options:Dict[str, Callable], *, 
                        show_before:List[Union[str, Callable]]=None, 
                        max_columns:int=None, borders:Dict[str, str]=None, selected_str=None, fill_before_menu=None,
                        choose_str:str=None):
        self.options = options

        if(show_before is not None):
            self.show_before = show_before
        if(max_columns is not None):
            self.max_columns = max_columns
        if(borders is not None):
            self.borders = borders
        if(selected_str is not None):
            self.selected_str = selected_str
        if(fill_before_menu is not None):
            self.fill_before_menu = fill_before_menu
        if(choose_str is not None):
            self.choose_str = choose_str

        self.pre_generate()

    def pre_generate(self):
        t_format = "{0:^"+str(self.ter_size.columns//self.max_columns)+"}"

        for opt in self.options.keys():
            self.unselected_options.append(t_format.format(opt))
            self.selected_options.append(t_format.format(self.selected_str+opt))

        self.__generated_columns = self.max_columns

    def __call__(self):
        t_cols = self.ter_size.columns
        t_rows = self.ter_size.lines
        t_format = "{0:^"+str(t_cols)+"}"

        if(self.show_before is not None):
            # Add the graphics to be shown before the menu. 
            self.__generated_menu.extend('\n'.join(t_format.format(line, 'centered') 
                                        for line in 
                                            (text.split('\n') if type(text) == str else text().split('\n'))
                                        
                                        for text in self.show_before))

            if(len(self.__generated_menu)-1 > t_rows): 
                raise Warning(f"The menu will clip due to max lines exceeded ({len(self.__generated_menu)-1}, max:{t_rows})\n"
                                "\t[Detected before adding the menu]")

        if(self.max_columns != self.__generated_columns):
            self.pre_generate()

        menu = []
        menu.append(f"{self.borders.get('UL')}{self.borders.get('Up')*(t_cols-2)}{self.borders.get('UR')}\n{self.borders.get('Left')}")
        sel_opt = self.selected_options[]
        unsel_opt_iter = iter(self.unselected_options+([""]*(self.max_columns-1)))
        menu.extend(f"{self.borders.get('Right')}\n{self.borders.get('Left')}".join(
            ''.join((unsel_opt_iter if col else '???') for col in range(self.max_columns))
        ))
        menu.append(f"{self.borders.get('Right')}\n{self.borders.get('DL')}{self.borders.get('Down')*(t_cols-2)}{self.borders.get('DR')}\n")

        spare_rows = len(self.__generated_menu)+len(menu)-1-t_rows
        if(spare_rows < 1): 
            raise Warning(f"The menu will clip due to max lines exceeded ({len(self.__generated_menu)-1}, max:{t_rows})\n"
                                "\t[Detected after adding the menu]")
        elif(spare_rows > 2):
            pass

        if(spare_rows == 2):
            menu.append('\n')
        #if()

