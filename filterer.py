import random
from time import sleep
import effects

def filter_topic(questionDict):
    effects.typer("What topic would you like to play?\n")
    # Create a list of topics so we can refer to them by index
    topics = list(questionDict.keys())
    
    # Print the topics with corresponding numbers
    for i, topic in enumerate(topics, start=1):
        effects.opps(f"({i}) {topic}")
    print("")

    
    # Ask the user to input a number corresponding to the topic
    topic_number = (input(":").strip())
    print("")
    
    # Check if the number is within the range of available topics
    while True:
        if topic_number.isdigit():
            topic_number = int(topic_number)
            if 1 <= topic_number <= len(topics):
                # Get the topic name using the input number (1-indexed)
                topic = topics[topic_number - 1]
                sleep (1)
                return topic
            
            else:
                effects.red("Invalid topic number. Please choose a valid number.")
                topic_number = (input(":").strip())
                print("")
        
        else:
            effects.red("Invalid topic number. Please choose a valid number.")
            topic_number = (input(":").strip())
            print("")
    

def show_questions(topic, questionDict, score, max_score):
    i = 1
    if topic in questionDict:
        
        effects.gold(f"Questions for topic: {topic}\n")
        sleep(.5)
        questions = questionDict[topic]
        random.shuffle(questions)

        for question in questions:
            effects.purp(question["question"])
            sleep(.25)
            # Shuffle the options randomly
            options = question["options"]
            correct_answer = question["answer"]
            options.append(correct_answer)
            random.shuffle(options)
            
            # Display the options
            for i, option in enumerate(options, 1):
                effects.opps(f"({i}) {option}")
                
            answer = effects.ans(":").strip()
            
            # Check if the user's answer is correct
            correct_option = question["answer"]
            while True:
                if answer.isdigit() and 1 <= int(answer) <= len(options):
                    if options[int(answer) - 1] == correct_option:
                        effects.gold("Correct!\n")
                        score += 1
                        max_score += 1
                        effects.scoring(f"Your score is {score}/{max_score}\n")
                        break
                    elif options[int(answer) - 1] != correct_option:
                        effects.gold("Wrong!\n")
                        max_score += 1
                        effects.scoring(f"Your score is {score}/{max_score}\n")
                        break
                else:
                    effects.red("Invalid answer. Please choose a valid answer.\n")
                    answer = effects.ans(":").strip()

                i = 1
    else:
        effects.red("No questions available for this topic.")
        