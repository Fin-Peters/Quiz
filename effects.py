from terminaltexteffects.effects.effect_laseretch import LaserEtch
from terminaltexteffects.effects.effect_errorcorrect import ErrorCorrect
from terminaltexteffects.utils.graphics import Gradient, Color

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


def opps(prompt_text):
    col = Color("0da5eb")
    effect = ErrorCorrect(prompt_text)
    effect.effect_config.final_gradient_stops = (col)
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
    print("")

