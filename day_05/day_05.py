#!/usr/bin/env python3
import sys

file_in = "input.txt"

def get_input():
    instruction_set = []
    with open(file_in) as fi:
        instructions = fi.readlines()[10::]
    
    for instruction in instructions:
        instruction = instruction.rstrip().strip("move ").replace("from ", "").replace("to ", "")
        instruction = instruction.split(" ", maxsplit=-1)
        instruction_set.append(instruction)
    return instruction_set

def move_multiple_containers(instruction_set):
    stacks = {1: ['R', 'N', 'P', 'G'],
            2: ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
            3: ['T', 'D', 'B', 'M', 'N', 'L'],
            4: ['R', 'V', 'P', 'S', 'B'],
            5: ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
            6: ['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
            7: ['F', 'Q', 'L'],
            8: ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
            9: ['L', 'P', 'B', 'V', 'M', 'J', 'F']}
    
    for instruction in instruction_set:
        stack_to_move = list()
        boxes_to_move = int(instruction[0])
        for box in range(boxes_to_move, 0, -1):
            stack_to_move.extend(stacks[int(instruction[1])][-box])
            stacks[int(instruction[1])].pop(-box)
        # stacks[int(instruction[1])].pop(x for x in range(-1, -boxes_to_move - 1, -1))
        stacks[int(instruction[2])].extend(stack_to_move)
    print(stacks)

def move_containers(instruction_set):
    stacks = {1: ['R', 'N', 'P', 'G'],
              2: ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'],
              3: ['T', 'D', 'B', 'M', 'N', 'L'],
              4: ['R', 'V', 'P', 'S', 'B'],
              5: ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'],
              6: ['W', 'Q', 'S', 'C', 'D', 'B', 'J'],
              7: ['F', 'Q', 'L'],
              8: ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'],
              9: ['L', 'P', 'B', 'V', 'M', 'J', 'F']}
    
    for instruction in instruction_set:
        for box in range(int(instruction[0]), 0, -1):
            box_to_move = stacks[int(instruction[1])].pop()
            print(box_to_move)
            stacks[int(instruction[2])].append(box_to_move)

    print(stacks)

if __name__ == '__main__':
    instruction_set = get_input()
    # move_containers(instruction_set)
    move_multiple_containers(instruction_set)


