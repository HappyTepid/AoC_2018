import os


def solve_examples(input_string):
    components = input_string.split(', ')
    components = [int(c) for c in components]
    return sum(components)

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(BASE_DIR, 'part_1_input.txt')
    with open(filepath, "r") as f:
        array = []
        for line in f:
            array.append(int(line.strip('\n')))
        print(sum(array))
