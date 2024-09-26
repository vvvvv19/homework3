# 检查答案的正确性
def check_answers(exercise_file, answer_file):
    # 打开题目文件和答案文件
    with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
        exercises = ef.readlines()  # 读取所有题目
        answers = af.readlines()  # 读取所有答案

    correct = []  # 用于保存正确的题目索引
    wrong = []    # 用于保存错误的题目索引

    # 遍历题目和答案进行检查
    for i, (exercise, answer) in enumerate(zip(exercises, answers)):
        # 计算题目的期望答案
        expected_answer = str(eval(exercise.replace('/', '/')))
        # 检查计算的答案是否与给定的答案匹配
        if expected_answer.strip() == answer.strip():
            correct.append(i + 1)  # 如果正确，记录题目索引（从1开始）
        else:
            wrong.append(i + 1)  # 如果错误，记录题目索引（从1开始）

    return correct, wrong  # 返回正确和错误的题目索引列表
