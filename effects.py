from terminaltexteffects.effects.effect_laseretch import LaserEtch
from terminaltexteffects.effects.effect_wipe import Wipe
from terminaltexteffects.effects.effect_print import Print
from terminaltexteffects.utils.graphics import Gradient, Color

import sys
from time import sleep  
import tkinter as tk
import os

# re-usable code block for tte also the intro
def intro(prompt_text):
    effect = LaserEtch(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            #sys.stdout.flush()
            sleep(.01)
    print("")


def opps(prompt_text):
    col = "0da5eb" 
    rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    
    # ANSI escape sequence for RGB color
    color_start = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    color_end = "\033[0m"  # Reset color to default

    for char in prompt_text:
            sys.stdout.write(color_start + char + color_end)
            sys.stdout.flush()
            sleep(.05)
    print("")

def ans(prompt_text: str):
    effect = Print(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
            
            
    return input("")
