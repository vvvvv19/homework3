import random
from fractions import Fraction
import format_mixed_number as mixed

# 生成四则运算题目
def generate_exercises(num_questions, range_limit):
    # 定义运算符
    operators = ['+', '-', '*', '/']
    exercises = set()  # 用于保存生成的表达式
    formatted_exercises = set()  # 用于保存带分数形式的题目

    # 生成题目，直到达到要求的数量
    while len(exercises) < num_questions:
        num_operands = random.randint(2, 4)  # 随机确定运算数的数量
        nums = []  # 用于保存运算数
        formatted_nums = []  # 用于保存格式化的运算数

        # 生成运算数
        for _ in range(num_operands):
            if random.choice([True, False]):
                # 生成整数
                num = random.randint(1, range_limit)
                nums.append(str(num))
                formatted_nums.append(str(num))
            else:
                # 生成分数
                numerator = random.randint(1, range_limit - 1)
                denominator = random.randint(2, range_limit)
                fraction = Fraction(numerator, denominator)  # 创建分数对象
                formatted_fraction = mixed.format_mixed_number(fraction)  # 格式化为真分数
                nums.append(f"({fraction})")  # 将分数添加到运算数列表
                formatted_nums.append(f"({formatted_fraction})")  # 添加格式化的分数

        random_ops = random.choices(operators, k=num_operands - 1)  # 随机选择运算符

        # 创建表达式
        expr = nums[0]  # 表达式初始化为第一个运算数
        formatted_expr = formatted_nums[0]  # 格式化表达式初始化为第一个运算数
        for i in range(num_operands - 1):
            if random_ops[i] in ['+', '-']:
                # 对于加法和减法，添加括号以控制计算顺序
                expr = f"({expr} {random_ops[i]} {nums[i + 1]})"
                formatted_expr = f"({formatted_expr} {random_ops[i]} {formatted_nums[i + 1]})"
            else:
                # 对于乘法和除法，不添加括号
                expr += f" {random_ops[i]} {nums[i + 1]}"
                formatted_expr += f" {random_ops[i]} {formatted_nums[i + 1]}"

        # 去掉最外层的括号
        if expr.startswith('(') and expr.endswith(')'):
            expr = expr[1:-1]
        if formatted_expr.startswith('(') and formatted_expr.endswith(')'):
            formatted_expr = formatted_expr[1:-1]

        # 计算结果并检查是否为负数
        try:
            result = eval(expr)
            if result < 0:  # 如果结果为负数，跳过当前题目
                continue
        except ZeroDivisionError:  # 处理除零异常
            continue
        except SyntaxError:  # 处理语法错误
            continue

        exercises.add(expr)  # 添加表达式到题目集合
        formatted_exercises.add(formatted_expr)  # 添加格式化的题目到集合

    return list(exercises), list(formatted_exercises)  # 返回题目和格式化题目的列表
