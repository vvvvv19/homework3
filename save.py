# 保存题目到文件
def save_exercises(formatted_exercises):
    with open('FormattedExercises.txt', 'w') as f:
        for exercise in formatted_exercises:
            f.write(f"{exercise}\n")  # 每道题目占一行

# 保存答案到文件
def save_answers(answers):
    with open('Answers.txt', 'w') as f:
        for answer in answers:
            f.write(answer + '\n')  # 每个答案占一行