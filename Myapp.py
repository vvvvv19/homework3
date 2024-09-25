import argparse

def generate_questions(num):
    for i in range(num):
        print(f"Question {i + 1}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, required=True, help='Number of questions to generate')
    args = parser.parse_args()

    generate_questions(args.n)
