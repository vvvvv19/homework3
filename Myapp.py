import argparse
import random

def main():
    parser = argparse.ArgumentParser(description='生成数学题目。')
    parser.add_argument('-n', type=int, required=True, help='生成题目的数量')
    parser.add_argument('-r', type=int, required=True, help='题目中数值的范围')

if __name__ == '__main__':
    main()
