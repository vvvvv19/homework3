from fractions import Fraction
import format_mixed_number as mixed


# 计算题目的答案
def calculate_answers(exercises):
    answers = []
    for expr in exercises:
        result = eval(expr)
        answers.append(mixed.format_mixed_number(Fraction(result).limit_denominator()))
    return answers