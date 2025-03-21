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
    col = Color("0da5eb")
    effect = Wipe(prompt_text)
    effect.effect_config.final_gradient_stops = (col)
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            effect.effect_config.frame_count = 10
            #effect.effect_config.animation_speed = 200
            #sys.stdout.flush()
            #sleep(.01)
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
