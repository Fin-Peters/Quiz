import reader
import filterer
import os
import ending

filePath = "CombinedQuiz.json"
questionDict = reader.reader(filePath)
score = 0
max_score = 0
redo = False

def main():
    # clears terminal
    os.system('cls||clear')
    topic = filterer.filter_topic(questionDict )
    filterer.show_questions(topic, questionDict, score, max_score )
    ending.ending(score, max_score, redo)
    if redo == True:
        main()


main()
