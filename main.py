import intro
import os
import reader

def filter_topic():
    print("What topic would you like to play? (1) History\n (2) Chemistry\n (3) Biology\n (4) Games\n (5) General")
    topic = input(":")
    return topic

def main():
    filePath = "CombinedQuiz.json"
    questionDict = reader.reader(filePath)
    topic = filter_topic()