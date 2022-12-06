#!/usr/bin/env python3

def first_marker(problem_input, num_unique):
    for i in range(num_unique, len(problem_input)):
        if len(set(problem_input[i - num_unique:i])) == num_unique:
            print(i)
            return
    assert False

def part1(problem_input):
    first_marker(problem_input, 4)

def part2(problem_input):
    first_marker(problem_input, 14)

def main():
    with open('input') as f:
        problem_input = f.read()
    print('Part 1: ', end='')
    part1(problem_input)
    print('Part 2: ', end='')
    part2(problem_input)

if __name__ == '__main__':
    main() 
