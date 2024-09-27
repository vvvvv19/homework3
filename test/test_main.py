import unittest
from fractions import Fraction
import random
from main import (format_mixed_number,generate_exercises,calculate_answers,
                   save_exercises,save_formatted_exercises,save_answers,check_answers,
                   save_grade)



class TestMathExercises(unittest.TestCase):

    #测试格式化函数 该测试结果应为不通过
    def test_format_mixed_number(self):
        self.assertEqual(format_mixed_number(Fraction(5, 2)), "2'1/2")
        self.assertEqual(format_mixed_number(Fraction(3, 1)), "3")
        self.assertEqual(format_mixed_number(Fraction(1, 3)), "1/3")
        self.assertEqual(format_mixed_number(Fraction(-3, 2)), "-1'1/2")
        self.assertEqual(format_mixed_number(Fraction(0, 1)), "0")

    #测试生成题目函数生成的题目数量
    def test_generate_exercises(self):
        exercises, formatted_exercises = generate_exercises(5, 10)
        self.assertEqual(len(exercises), 5)
        self.assertEqual(len(formatted_exercises), 5)

        for exercise in exercises:
            self.assertTrue(any(op in exercise for op in ['+', '-', '*', '/']))

    #测试答案函数计算的答案是否正确 该测试结果应为不通过
    def test_calculate_answers(self):
        exercises = ["2 + 3", "(1 + 1) * 5", "5 - 3", "7 / 1"]
        answers = calculate_answers(exercises)
        expected_answers = ["5", "2", "2", "7"]
        self.assertEqual(answers, expected_answers)

    #测试检查答案函数输出是否正确 该测试结果应为不通过
    def test_check_answers(self):
        with open('Exercises_test.txt', 'w') as ef:
            ef.write("2 + 3\n(1 + 1) * 5\n")
        with open('Answers_test.txt', 'w') as af:
            af.write("5\n2\n")

        correct, wrong = check_answers('Exercises_test.txt', 'Answers_test.txt')
        self.assertEqual(correct, [1, 2])
        self.assertEqual(wrong, [])

    #测试保存文件函数
    def test_save_grade(self):
        correct = [1, 2]
        wrong = [3]
        save_grade(correct, wrong)  # 无异常则通过

    #测试算数结果是否非负
    def test_generate_exercises_negative(self):
        exercises, _ = generate_exercises(100, 10)  # 假设生成100道题目
        self.assertTrue(all(eval(ex) >= 0 for ex in exercises))

    #测试验证格式化函数在处理边界情况时的正确性
    def test_format_mixed_number_edge_cases(self):
        self.assertEqual(format_mixed_number(Fraction(1, 1)), "1")
        self.assertEqual(format_mixed_number(Fraction(10, 3)), "3'1/3")
        self.assertEqual(format_mixed_number(Fraction(-10, 3)), "-3'1/3")

    #测试生成函数函数在处理较大范围时的正确性
    def test_generate_exercises_with_large_range(self):
        exercises, formatted_exercises = generate_exercises(5, 100)
        self.assertEqual(len(exercises), 5)
        self.assertTrue(all(eval(ex) <= 100 for ex in exercises))

    #测试计算答案函数在处理包含分数的算式时的正确性
    def test_calculate_answers_with_fractions(self):
        exercises = ["1/2 + 1/4", "3/4 - 1/2", "2 * 3/4", "5 / (1/5)"]
        answers = calculate_answers(exercises)
        expected_answers = ["3/4", "1/4", "1'1/2", "25"]
        self.assertEqual(answers, expected_answers)

    #测试答案正确检测函数在用户答案错误时的行为
    def test_check_answers_incorrect(self):
        with open('Exercises_test.txt', 'w') as ef:
            ef.write("2 + 3\n(1 + 1) * 5\n")
        with open('Answers_test.txt', 'w') as af:
            af.write("4\n3\n")  # 错误答案

        correct, wrong = check_answers('Exercises_test.txt', 'Answers_test.txt')
        self.assertEqual(correct, [])
        self.assertEqual(wrong, [1, 2])


if __name__ == "__main__":
    unittest.main()

