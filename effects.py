from terminaltexteffects.effects.effect_laseretch import LaserEtch

import sys
from time import sleep  
import tkinter as tk
import os

# re-usable code block for tte 
def intro(prompt_text):
    effect = LaserEtch(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            #sys.stdout.flush()
            
    print("")
# clears terminal
os.system('cls||clear')

intro(" ██████╗ ██╗   ██╗██╗███████╗██╗ ██████╗ █████╗ ██╗          ██████╗ ██╗   ██╗██╗███████╗███████╗███████╗██████╗\n██╔═══██╗██║   ██║██║╚══███╔╝██║██╔════╝██╔══██╗██║         ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗\n██║   ██║██║   ██║██║  ███╔╝ ██║██║     ███████║██║         ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ █████╗  ██████╔╝\n██║▄▄ ██║██║   ██║██║ ███╔╝  ██║██║     ██╔══██║██║         ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗\n╚██████╔╝╚██████╔╝██║███████╗██║╚██████╗██║  ██║███████╗    ╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗██║  ██║\n ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\n")
sleep(1)