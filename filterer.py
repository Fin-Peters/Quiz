import random
from time import sleep
from effects import opps
from effects import ans


def filter_topic(questionDict):
    print("What topic would you like to play?")
    # Create a list of topics so we can refer to them by index
    topics = list(questionDict.keys())
    
    # Print the topics with corresponding numbers
    for i, topic in enumerate(topics, start=1):
        print(f"({i}) {topic}")

    
    # Ask the user to input a number corresponding to the topic
    topic_number = int(input(":").strip())
    
    # Check if the number is within the range of available topics
    if 1 <= topic_number <= len(topics):
        # Get the topic name using the input number (1-indexed)
        topic = topics[topic_number - 1]
        sleep (1)
        return topic
    
    else:
        print("Invalid topic number. Please choose a valid number.")
        return filter_topic(questionDict)
    

def show_questions(topic, questionDict, score, max_score):
    i = 1
    if topic in questionDict:
        
        print(f"Questions for topic: {topic}")
        
        questions = questionDict[topic]
        random.shuffle(questions)

        for question in questions:
            print(question["question"])
            
            # Shuffle the options randomly
            options = question["options"]
            correct_answer = question["answer"]
            options.append(correct_answer)
            random.shuffle(options)
            
            # Display the options
            for i, option in enumerate(options, 1):
                opps(f"({i}) {option}")
                
            answer = ans(":").strip()
            
            # Check if the user's answer is correct
            correct_option = question["answer"]
            if answer.isdigit():
                if options[int(answer) - 1] == correct_option:
                    print("Correct!\n")
                    score += 1
                    max_score += 1
                elif options[int(answer) - 1] != correct_option:
                    print("Wrong!\n")
                    max_score += 1
            else:
                print("Invalid answer. Please choose a valid answer.\n")
                answer = ans(":").strip()

            print(f"Your score is {score}/{max_score}\n")

            i = 1
    else:
        print("No questions available for this topic.")
        return filter_topic(questionDict)