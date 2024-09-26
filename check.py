# 检查答案的正确性
def check_answers(exercise_file, answer_file):
    with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
        exercises = ef.readlines()
        answers = af.readlines()

    correct = []
    wrong = []

    for i, (exercise, answer) in enumerate(zip(exercises, answers)):
        expected_answer = str(eval(exercise.replace('/', '/')))
        if expected_answer.strip() == answer.strip():
            correct.append(i + 1)
        else:
            wrong.append(i + 1)

    return correct, wrong