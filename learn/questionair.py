class Question:
    def __init__(self, prompt, answer):
        self.question_asked = prompt
        self.answer_of_question = answer


question_promts = [
    "what is the colour of apple \n a)red b)magenta c)yellow \n",
    "what is the colour of strawberry \n a)red b)magenta c)yellow \n",
    "what is the colour of mango \n a)red b)magenta c)yellow \n"
]

questions = [
    Question(question_promts[0], 'a'),
    Question(question_promts[1], 'a'),
    Question(question_promts[2], 'c')
]


def run_test(question_list):
    score = 0
    for sawal in question_list:
        answer = input(sawal.question_asked)
        if answer == sawal.answer_of_question:
            score += 1
    print("you score " + str(score) + "/" + str(len(questions)))


run_test(questions)
