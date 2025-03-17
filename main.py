import intro
import os
import reader

i = 0
def filter_topic():
    filePath = "CombinedQuiz.json"
    questionDict = reader.reader(filePath)
    print("What topic would you like to play?")
    for topic in questionDict.keys():
        print(f"({i}) {topic}")
        i += i
    topic = input(":")
    return topic

def main():
    filePath = "CombinedQuiz.json"
    questionDict = reader.reader(filePath)
    topic = filter_topic()

filter_topic()
main()