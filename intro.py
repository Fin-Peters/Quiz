from terminaltexteffects.effects.effect_vhstape import VHSTape

import sys
from time import sleep  
import tkinter as tk
import os

# re-usable code block for tte 
def custom_type(prompt_text):
    effect = VHSTape(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            #sys.stdout.flush()
            
    print("")
# clears terminal
os.system('cls||clear')

custom_type(" ██████╗ ██╗   ██╗██╗███████╗██╗ ██████╗ █████╗ ██╗          ██████╗ ██╗   ██╗██╗███████╗███████╗███████╗██████╗\n██╔═══██╗██║   ██║██║╚══███╔╝██║██╔════╝██╔══██╗██║         ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗\n██║   ██║██║   ██║██║  ███╔╝ ██║██║     ███████║██║         ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ █████╗  ██████╔╝\n██║▄▄ ██║██║   ██║██║ ███╔╝  ██║██║     ██╔══██║██║         ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗\n╚██████╔╝╚██████╔╝██║███████╗██║╚██████╗██║  ██║███████╗    ╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗██║  ██║\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\n")
sleep(1)