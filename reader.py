import json
#makes json file readable
def reader(filePath):
    with open(filePath, "r") as file:
        questionDict = json.load(file)
    return questionDict