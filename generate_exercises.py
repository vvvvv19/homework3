import random

# 生成四则运算题目
def generate_exercises(num_questions, range_limit):
    operators = ['+', '-', '*', '/']  # 可用运算符
    exercises = set()  # 使用集合避免重复题目

    while len(exercises) < num_questions:  # 直到生成足够的题目
        # 随机生成操作数
        nums = [random.randint(1, range_limit - 1) for _ in range(3)]
        # 随机选择2个运算符
        random_ops = random.sample(operators, k=2)

        # 进行运算并检查负数
        # 使用运算符顺序来决定
        if random_ops[0] == '-' and nums[0] < nums[1]:
            continue  # 保证 a - b >= 0
        if random_ops[1] == '/' and nums[2] == 0:
            continue  # 避免除以零

        # 生成题目字符串
        expr = f"{nums[0]} {random_ops[0]} {nums[1]} {random_ops[1]} {nums[2]}"
        exercises.add(expr)

    return list(exercises)  # 返回生成的题目