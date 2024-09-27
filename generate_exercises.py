import random
from fractions import Fraction
import format_mixed_number as mixed

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
                formatted_fraction = mixed.format_mixed_number(fraction)
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
