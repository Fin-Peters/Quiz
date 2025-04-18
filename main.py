import reader
import filterer
import os
import ending
import effects

filePath = "CombinedQuiz.json"
questionDict = reader.reader(filePath)


def main():
    #needs to be here for game looping to not act weird
    redo = False
    incorrects = []
    score = 0
    max_score = 0
    # clears terminal
    os.system('cls||clear')
    effects.intro(" ██████╗ ██╗   ██╗██╗███████╗███████╗██╗ ██████╗ █████╗ ██╗          ██████╗ ██╗   ██╗██╗███████╗███████╗███████╗██████╗ ███████╗\n██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██║██╔════╝██╔══██╗██║         ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗██╔════╝\n██║   ██║██║   ██║██║  ███╔╝   ███╔╝ ██║██║     ███████║██║         ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ █████╗  ██████╔╝███████╗\n██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██║██║     ██╔══██║██║         ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗╚════██║\n╚██████╔╝╚██████╔╝██║███████╗███████╗██║╚██████╗██║  ██║███████╗    ╚██████╔╝╚██████╔╝██║███████╗███████╗███████╗██║  ██║███████║\n╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝\n")
    topic = filterer.filter_topic(questionDict )
    score, max_score, incorrects = filterer.show_questions(topic, questionDict, score, max_score, incorrects)
    redo = ending.ending(score, max_score, incorrects, redo)
    if redo == True:
        main()


main()
