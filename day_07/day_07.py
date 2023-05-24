#!/usr/bin/env python3

import sys

file_in = "./input.txt"

def get_input():
    with open (file_in) as fi:
        commands = fi.read().splitlines()
    return commands
    # print(commands)

def find_dirs(commands):
    # use dictionary maybe? look for dir, then ls to get subsequent dirs
    dirs = list()
    dir_dict = dict()


    for idx, command in enumerate(commands):
        if "$ ls" in command:
            dir_dict[commands[idx - 1][5::]] = {}
            while "$ cd" not in command:
                
                pass
            # dir_dict[command[5::]] = {x for x in commands while "dir" in x}
            print(idx, command)
    print(dir_dict)

    # for idx, command in enumerate(commands):
    #     if ("$ cd" in command) and (command[5::] != ".."):
    #         dir_dict[command[5::]] = {x for x in commands while "dir" in x}
    #         print(idx, command)

    # for idx, command in enumerate(commands):
    #     if "dir" in command:
    #         dir_dict[command[4::]] = dict()
    #         # dirs.append(command[4::])
    # print(dir_dict)

    # print(len(dir_dict))

    # iterate over commands again looking for cd followed by LS for nested dirs

if __name__ == '__main__':
    commands = get_input()
    find_dirs(commands)

