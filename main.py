import intro
import os
import reader


def filter_topic():
    filePath = "CombinedQuiz.json"
    i = 1
    questionDict = reader.reader(filePath)
    print("What topic would you like to play?")
    for topic in questionDict.keys():
        print(f"({i}) {topic}")
        i += 1
    topic = input(":")
    return topic

def main():
    filePath = "CombinedQuiz.json"
    questionDict = reader.reader(filePath)

filter_topic()
main()