import intro
import os
import reader
import filterer



def main():
    filterer.filter_topic()
    filePath = "CombinedQuiz.json"
    questionDict = reader.reader(filePath)



main()