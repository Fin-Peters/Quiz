import reader

def filter_topic(questionDict):
    print("What topic would you like to play?")
    # Create a list of topics so we can refer to them by index
    topics = list(questionDict.keys())
    
    # Print the topics with corresponding numbers
    for i, topic in enumerate(topics, start=1):
        print(f"({i}) {topic}")

    while True:
        try:
            # Ask the user to input a number corresponding to the topic
            topic_number = int(input(":").strip())
            
            # Check if the number is within the range of available topics
            if 1 <= topic_number <= len(topics):
                # Get the topic name using the input number (1-indexed)
                topic = topics[topic_number - 1]
                return topic
            else:
                print("Invalid topic number. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

            
def show_questions(topic, questionDict):

    if topic in questionDict:
        print(f"Questions for topic: {topic}")
        for question in questionDict[topic]:
            print(question)
    else:
        print("No questions available for this topic.")