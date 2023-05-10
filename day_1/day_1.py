#!/usr/bin/python3

from collections import defaultdict

input_file = "input.txt"

def read_input():
    with open(input_file) as file_in:
        f = file_in.read().splitlines()
    return f

def calc_most_calories(f):
    cal_count = 0
    elves = []
    for calorie in f:
        if calorie != '':
            cal_count += int(calorie)
        else:
            elves.append(cal_count)
            cal_count = 0
    elves.sort(reverse=True)
    print(elves[0])
    total_sum = elves[0] + elves[1] + elves[2]
    print(total_sum)


if __name__ == "__main__":
    f = read_input()
    calc_most_calories(f)
