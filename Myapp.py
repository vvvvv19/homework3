import argparse  # 用于解析命令行参数
import save as sa  # 导入保存模块
import check as check  # 导入检查模块
import generate_exercises as gen  # 导入生成题目的模块
import calculate_answers as cal  # 导入计算答案的模块

def myapp():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='四则运算题目生成器')
    # 添加命令行参数
    parser.add_argument('-n', type=int, help='生成题目的个数')  # 题目数量
    parser.add_argument('-r', type=int, help='题目中数值的范围')  # 数值范围
    parser.add_argument('-e', type=str, help='输入题目文件')  # 题目文件路径
    parser.add_argument('-a', type=str, help='输入答案文件')  # 答案文件路径

    args = parser.parse_args()  # 解析命令行参数

    # 如果提供了题目文件和答案文件，进行答案检查
    if args.e and args.a:
        correct, wrong = check.check_answers(args.e, args.a)  # 检查答案
        sa.save_grade(correct, wrong)  # 保存成绩
        return

    # 如果缺少必需的参数，抛出错误
    if args.n is None or args.r is None:
        parser.error("缺少必需的参数 -n 或 -r")

    # 生成题目和格式化题目
    exercises, formatted_exercises = gen.generate_exercises(args.n, args.r)
    answers = cal.calculate_answers(exercises)
    sa.save_exercises(exercises)
    sa.save_formatted_exercises(formatted_exercises)
    sa.save_answers(answers)

# 运行主函数
if __name__ == "__main__":
    myapp()

