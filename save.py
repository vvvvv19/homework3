# 保存题目到文件
def save_exercises(exercises):
    with open('Exercises.txt', 'w') as f:
        for exercise in exercises:
            f.write(f"{exercise}\n")  # 每道题目占一行

# 保存带分数形式的题目到文件
def save_formatted_exercises(formatted_exercises):
    with open('FormattedExercises.txt', 'w') as f:
        for exercise in formatted_exercises:
            f.write(f"{exercise}\n")  # 每道题目占一行

# 保存答案到文件
def save_answers(answers):
    with open('Answers.txt', 'w') as f:
        for answer in answers:
            f.write(answer + '\n')  # 每个答案占一行

# 输出检查结果到文件
def save_grade(correct, wrong):
    with open('Grade.txt', 'w') as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")