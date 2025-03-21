import reader
import filterer
import os

filePath = "CombinedQuiz.json"
questionDict = reader.reader(filePath)
score = 0
max_score = 0


def main():
    # clears terminal
    os.system('cls||clear')
    topic = filterer.filter_topic(questionDict )
    filterer.show_questions(topic, questionDict, score, max_score )



main()
