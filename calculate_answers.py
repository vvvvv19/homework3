from fractions import Fraction
import format_mixed_number as mixed

# 计算题目的答案
def calculate_answers(exercises):
    answers = []  # 用于保存每个题目的答案
    for expr in exercises:
        result = eval(expr)  # 计算表达式的结果
        # 将结果转换为分数并格式化为带分数
        answers.append(mixed.format_mixed_number(Fraction(result).limit_denominator()))
    return answers  # 返回答案列表
