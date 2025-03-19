import effects
import reader
import filterer

filePath = "CombinedQuiz.json"
questionDict = reader.reader(filePath)
score = 0
max_score = 0

def main():
    topic = filterer.filter_topic(questionDict )
    filterer.show_questions(topic, questionDict, score, max_score )



main()
