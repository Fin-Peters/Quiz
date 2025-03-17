import intro
import os
import reader
import filterer

filePath = "CombinedQuiz.json"
questionDict = reader.reader(filePath)


def main():
    topic = filterer.filter_topic(questionDict)
    filterer.show_questions(topic, questionDict)



main()