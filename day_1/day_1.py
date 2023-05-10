#!/usr/bin/python3

from collections import defaultdict

input_file = "input.txt"

def read_input():
    with open(input_file) as file_in:
        f = file_in.read().splitlines()
    return f



if __name__ == "__main__":
    f = read_input()
    elf = 1
    elves = defaultdict(int)
    for calorie in f:
        if calorie != '':
            elves[elf] += int(calorie)
        else:
            elf += 1

    most_calories = 0
    # print(elves.values())
    for cal_count in elves.values():
        print(cal_count)
        if cal_count > most_calories:
            most_calories = cal_count

    print(most_calories)

