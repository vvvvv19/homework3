from fractions import Fraction
import random
from line_profiler_pycharm import profile

# 格式化分数为带分数形式
@profile
def format_mixed_number(fraction):
    if fraction.denominator == 1:
        return str(fraction.numerator)  # 如果是整数，直接返回整数
    whole = fraction.numerator // fraction.denominator
    remainder = abs(fraction.numerator) % fraction.denominator
    if whole == 0:
        return str(fraction)  # 如果没有整数部分，直接返回分数
    elif remainder == 0:
        return str(whole)  # 如果没有余数，返回整数部分
    else:
        return f"{whole}'{remainder}/{fraction.denominator}"  # 返回带分数形式

@profile
# 生成四则运算题目
def generate_exercises(num_questions, range_limit):
    operators = ['+', '-', '*', '/']
    exercises = set()
    formatted_exercises = set()  # 用于保存带分数形式的题目

    while len(exercises) < num_questions:
        num_operands = random.randint(2, 4)
        nums = []
        formatted_nums = []
        for _ in range(num_operands):
            if random.choice([True, False]):
                num = random.randint(1, range_limit)
                nums.append(str(num))
                formatted_nums.append(str(num))
            else:
                numerator = random.randint(1, range_limit - 1)
                denominator = random.randint(2, range_limit)
                fraction = Fraction(numerator, denominator)
                formatted_fraction = format_mixed_number(fraction)
                nums.append(f"({fraction})")
                formatted_nums.append(f"({formatted_fraction})")

        random_ops = random.choices(operators, k=num_operands - 1)

        # 创建表达式
        expr = nums[0]
        formatted_expr = formatted_nums[0]
        for i in range(num_operands - 1):
            if random_ops[i] in ['+', '-']:
                expr = f"({expr} {random_ops[i]} {nums[i + 1]})"
                formatted_expr = f"({formatted_expr} {random_ops[i]} {formatted_nums[i + 1]})"
            else:
                expr += f" {random_ops[i]} {nums[i + 1]}"
                formatted_expr += f" {random_ops[i]} {formatted_nums[i + 1]}"

        # 去掉最外层的括号
        if expr.startswith('(') and expr.endswith(')'):
            expr = expr[1:-1]
        if formatted_expr.startswith('(') and formatted_expr.endswith(')'):
            formatted_expr = formatted_expr[1:-1]

        try:
            result = eval(expr)
            if result < 0:
                continue
        except ZeroDivisionError:
            continue
        except SyntaxError:
            continue

        exercises.add(expr)
        formatted_exercises.add(formatted_expr)

    return list(exercises), list(formatted_exercises)

@profile
# 计算题目的答案
def calculate_answers(exercises):
    answers = []
    for expr in exercises:
        result = eval(expr)
        answers.append(format_mixed_number(Fraction(result).limit_denominator()))
    return answers

@profile
# 保存题目到文件
def save_exercises(exercises):
    with open('Exercises.txt_for_test', 'w') as f:
        for exercise in exercises:
            f.write(f"{exercise}\n")  # 每道题目占一行

@profile
# 保存带分数形式的题目到文件
def save_formatted_exercises(formatted_exercises):
    with open('FormattedExercises_for_test.txt', 'w') as f:
        for exercise in formatted_exercises:
            f.write(f"{exercise}\n")  # 每道题目占一行

@profile
# 保存答案到文件
def save_answers(answers):
    with open('Answers_for_test.txt', 'w') as f:
        for answer in answers:
            f.write(answer + '\n')  # 每个答案占一行

@profile
# 检查答案的正确性
def check_answers(exercise_file, answer_file):
    with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
        exercises = ef.readlines()
        answers = af.readlines()

    correct = []
    wrong = []

    for i, (exercise, answer) in enumerate(zip(exercises, answers)):
        expected_answer = format_mixed_number(Fraction(eval(exercise.strip())).limit_denominator())
        if expected_answer.strip() == answer.strip():
            correct.append(i + 1)
        else:
            wrong.append(i + 1)

    return correct, wrong


@profile
def save_grade(correct, wrong):
    with open('Grade_for_test.txt', 'w') as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")

@profile
def test():
    # 固定生成题目的个数和数值范围
    num_questions = 10  # 生成10道题目
    range_limit = 10  # 数值范围为1到10

    # 生成题目
    exercises, formatted_exercises = generate_exercises(num_questions, range_limit)
    answers = calculate_answers(exercises)

    # 保存题目和答案到文件
    save_exercises(exercises)
    save_formatted_exercises(formatted_exercises)
    save_answers(answers)

    # 检查答案
    correct, wrong = check_answers('Exercises.txt_for_test', 'Answers_for_test.txt')

    # 输出检查结果到文件
    save_grade(correct, wrong)

    # 输出生成的题目和答案到控制台（可选）
    print("生成的题目:")
    for exercise in exercises:
        print(exercise)

    print("\n生成的答案:")
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    test()




