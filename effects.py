from terminaltexteffects.effects.effect_crumble import Crumble
from terminaltexteffects.effects.effect_sweep import Sweep
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_wipe import Wipe
from terminaltexteffects.effects.effect_print import Print


import sys
from time import sleep  


# re-usable code block for tte also the intro
def intro(prompt_text):
    effect = Burn(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        #makes the effect print out each frame
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
            sleep(0)

    print("")

def BigEnding(prompt_text):
    effect = Sweep(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
            sleep(.00001)
    print("")

def Ending(prompt_text):
    effect = Crumble(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
            sleep(.01)
    print("")

def typer(prompt_text):
    effect = Wipe(prompt_text)
    effect.effect_config.final_gradient_frames = 1
    with effect.terminal_output(end_symbol=" ") as terminal:
        for frame in effect:
            terminal.print(frame)
            sys.stdout.write("\033[K")
            sys.stdout.flush()
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

def scoring(prompt_text):
    col = "e28c1e" 
    rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    
    # ANSI escape sequence for RGB color
    color_start = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    color_end = "\033[0m"  # Reset color to default

    for char in prompt_text:
            sys.stdout.write(color_start + char + color_end)
            sys.stdout.flush()
            sleep(.005)
    print("")

def purp(prompt_text):
    col = "451eea" 
    rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    
    # ANSI escape sequence for RGB color
    color_start = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    color_end = "\033[0m"  # Reset color to default
    for char in prompt_text:
                sys.stdout.write(color_start + char + color_end)
                sys.stdout.flush()
                sleep(.005)
    print("")
   
def red(prompt_text):
    col = "dc143c" 
    rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    
    # ANSI escape sequence for RGB color
    color_start = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    color_end = "\033[0m"  # Reset color to default

    for char in prompt_text:
            sys.stdout.write(color_start + char + color_end)
            sys.stdout.flush()
            sleep(.005)
    print("")

def gold(prompt_text):
    col = "eec900" 
    rgb = tuple(int(col.lstrip("#")[i:i+2], 16) for i in (0, 2, 4))
    
    # ANSI escape sequence for RGB color
    color_start = f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    color_end = "\033[0m"  # Reset color to default

    for char in prompt_text:
            sys.stdout.write(color_start + char + color_end)
            sys.stdout.flush()
            sleep(.005)
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
