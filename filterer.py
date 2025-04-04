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

    
    topic_number = (input(":").strip())
    print("")
    
    # Check if the number is within the range of available topics
    while True:
        if topic_number.isdigit():
            topic_number = int(topic_number)
            if 1 <= topic_number <= len(topics):
                # Get the topic name using the input number (1-indexed) cause computer reading starts at 0
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
    if topic in questionDict:
        effects.gold(f"Questions for topic: {topic}\n")
        sleep(.5)
        
        # Shuffle the question order
        questions = questionDict[topic]
        random.shuffle(questions)

        for question in questions:
            effects.purp(question["question"])
            sleep(.25)
            
            # Shuffle the options randomly and add the correct answer
            options = question["options"] + [question["answer"]]
            random.shuffle(options)
            
            # Display the options
            for i, option in enumerate(options, 1):
                effects.opps(f"({i}) {option}")
            
            # Get the user's answer
            while True:
                answer = effects.ans(":").strip()
                if answer.isdigit() and 1 <= int(answer) <= len(options):
                    break
                else:
                    effects.red("Invalid answer. Please choose a valid answer.\n")
            
            # Check if the user's answer is correct
            if options[int(answer) - 1] == question["answer"]:
                effects.gold("Correct!\n")
                score += 1
            else:
                effects.gold("Wrong!\n")
            
            # Update max_score
            max_score += 1
            effects.scoring(f"Your score is {score}/{max_score}\n")
            sleep(.5)
    
    # Return the final score and max_score after all questions are processed
    return score, max_score
                
        