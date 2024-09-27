from fractions import Fraction
import random
from line_profiler_pycharm import profile


@profile
# 格式化分数为带分数形式
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
    exercise_pairs = []  # 用于保存题目及其带分数形式的元组

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
                #分子
                numerator = random.randint(1, range_limit - 1)
                #分母
                denominator = random.randint(2, range_limit)
                fraction = Fraction(numerator, denominator)
                #变成代分数
                formatted_fraction = format_mixed_number(fraction)
                nums.append(f"{fraction}")
                formatted_nums.append(f"{formatted_fraction}")

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
        exercise_pairs.append((expr, formatted_expr))  # 保存元组

    # 分离出题目和带分数形式
    exercises, formatted_exercises = zip(*exercise_pairs) if exercise_pairs else ([], [])

    return list(exercises), list(formatted_exercises)


@profile
# 计算题目的答案
def calculate_answers(exercises):
    answers = []
    for expr in exercises:
        #使用eval计算字符串得到答案
        result = eval(expr)
        #将答案转化成代分数
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
        #读取题目和答案
        exercises = ef.readlines()
        answers = af.readlines()

    correct = []    # 存储正确答案的题目索引
    wrong = []      # 存储错误答案的题目索引

    # 遍历每个题目和对应的答案并组成元组生成索引
    for i, (exercise, answer) in enumerate(zip(exercises, answers)):
        # 计算题目的期望答案，并格式化为带分数形式
        expected_answer = format_mixed_number(Fraction(eval(exercise.strip())).limit_denominator())
        # 检查期望答案与用户答案是否匹配
        if expected_answer.strip() == answer.strip():
            correct.append(i + 1)#正确的加入正确列表
        else:
            wrong.append(i + 1)#错误的加入错误列表

    return correct, wrong


@profile
#判定文件写入生成
def save_grade(correct, wrong):
    with open('Grade_for_test.txt', 'w') as f:
        f.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        f.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")

@profile
def main():
    # 固定生成题目的个数和数值范围
    num_questions = 5  # 生成10道题目
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

    print("\n给人看的题目:")
    for formatted_exercise in formatted_exercises:
        print(formatted_exercise)

    print("\n生成的答案:")
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()




