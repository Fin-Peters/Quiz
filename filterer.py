import reader

def filter_topic(questionDict):
    i = 1
    print("What topic would you like to play?")
    for topic in questionDict.keys():
        print(f"({i}) {topic}")
        i += 1
    topic = input(":").strip()
    if topic not in questionDict.keys():
        print("Invalid topic")
        filter_topic(questionDict)
    return topic

def show_questions(topic, questionDict):

    if topic in questionDict:
        print(f"Questions for topic: {topic}")
        for question in questionDict[topic]:
            print(question)
    else:
        print("No questions available for this topic.")