import json

def reader(filePath):
    with open(filePath "r") as file:
        questionDict = json.load(file)
    return questionDict