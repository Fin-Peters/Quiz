import random
from time import sleep
from effects import opps
from effects import ans
from effects import typer
from effects import scoring
from effects import purp
from effects import gold

def filter_topic(questionDict):
    typer("What topic would you like to play?\n")
    # Create a list of topics so we can refer to them by index
    topics = list(questionDict.keys())
    
    # Print the topics with corresponding numbers
    for i, topic in enumerate(topics, start=1):
        opps(f"({i}) {topic}")
    print("")

    
    # Ask the user to input a number corresponding to the topic
    topic_number = int(input(":").strip())
    print("")
    
    # Check if the number is within the range of available topics
    while True:
        if topic_number.is_integer():
            if 1 <= topic_number <= len(topics):
                # Get the topic name using the input number (1-indexed)
                topic = topics[topic_number - 1]
                sleep (1)
                return topic
            
            else:
                gold("Invalid topic number. Please choose a valid number.")
                topic_number = int(input(":").strip())
                print("")
        
        else:
            gold("Invalid topic number. Please choose a valid number.")
            topic_number = int(input(":").strip())
            print("")
    

def show_questions(topic, questionDict, score, max_score):
    i = 1
    if topic in questionDict:
        
        gold(f"Questions for topic: {topic}\n")
        sleep(.5)
        questions = questionDict[topic]
        random.shuffle(questions)

        for question in questions:
            purp(question["question"])
            sleep(.25)
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
            while True:
                if answer.isdigit() and 1 <= int(answer) <= len(options):
                    if options[int(answer) - 1] == correct_option:
                        gold("Correct!\n")
                        score += 1
                        max_score += 1
                        break
                    elif options[int(answer) - 1] != correct_option:
                        gold("Wrong!\n")
                        max_score += 1
                        break
                else:
                    print("Invalid answer. Please choose a valid answer.\n")
                    answer = ans(":").strip()

                scoring(f"Your score is {score}/{max_score}\n")

                i = 1
    else:
        print("No questions available for this topic.")
        