import effects

def ending(score, max_score,incorrects, redo ):
    if score == max_score:
        effects.gold("Congratulations! You got a perfect score!\n")
        effects.BigEnding("██████╗ ███████╗ █████╗ ███╗   ██╗    ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗\n██╔══██╗██╔════╝██╔══██╗████╗  ██║    ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝\n██████╔╝█████╗  ███████║██╔██╗ ██║    █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗\n██╔══██╗██╔══╝  ██╔══██║██║╚██╗██║    ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║\n██████╔╝███████╗██║  ██║██║ ╚████║    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝\n╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝\n ")
    elif score == 1 or score == 0:
        effects.red("You... completed the quiz?\n")
        effects.scoring(f"Your final score is {score}/{max_score}\n")
        effects.Ending("██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗    ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗\n██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║    ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝\n██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║    █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗\n██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║    ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║\n██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝\n╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝\n")
        
    else:
        effects.red("You have completed the quiz!\n")
        effects.scoring(f"Your final score is {score}/{max_score}\n")
        effects.intro("███╗   ██╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ██╗         ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗\n████╗  ██║██╔═══██╗██╔══██╗████╗ ████║██╔══██╗██║         ██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝\n██╔██╗ ██║██║   ██║██████╔╝██╔████╔██║███████║██║         █████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗\n██║╚██╗██║██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║██║         ██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║\n██║ ╚████║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝\n╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝\n ")

    while True:
        effects.purp("Would you like to see the incorrect answers? (yes/no): ")
        show_incorrect = effects.ans(": ").strip().lower()
        if show_incorrect == "yes":
            effects.red("Incorrect answers:\n")
            for question in incorrects:
                effects.red(question)
            break
        elif show_incorrect == "no":
            break
        else:
            effects.red("Invalid input. Please choose a valid answer.\n")

    while True:
        
        retry = effects.ans("Do you want to play again? (yes/no): ").strip().lower()
        if retry == "yes":
            redo = True
            return redo
        elif retry == "no":
            effects.gold("Goodbye!\n")
            return False
            
        else:
            effects.red("Invalid input. Please choose a valid answer.\n")

