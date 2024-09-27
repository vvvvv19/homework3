import format_mixed_number as mixed
from fractions import Fraction


def check_answers(exercise_file, answer_file):
    # 打开题目文件和答案文件
    with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
        exercises = ef.readlines()  # 读取所有题目
        answers = af.readlines()  # 读取所有答案

    correct = []  # 用于存储正确的题目编号
    wrong = []  # 用于存储错误的题目编号

    # 遍历每道题目和对应的答案
    for i, (exercise, answer) in enumerate(zip(exercises, answers)):
        # 计算当前题目的预期答案
        expected_answer = mixed.format_mixed_number(Fraction(eval(exercise.strip())).limit_denominator())

        # 检查预期答案是否与提供的答案匹配
        if expected_answer.strip() == answer.strip():
            correct.append(i + 1)  # 如果匹配，将题目编号添加到正确列表
        else:
            wrong.append(i + 1)  # 如果不匹配，将题目编号添加到错误列表

    return correct, wrong  # 返回正确和错误的题目编号列表

