#!/usr/bin/python3
import string

file_in = "input.txt"

def get_input():
    with open(file_in) as fi:
        rucksack = fi.read().splitlines()
    return rucksack

def elf_groups(gift_coll):
    common = list()
    priority_sum = 0
    print(gift_coll[0])
    for i in range(0, len(gift_coll) - 2, 3):
        for letter in gift_coll[i]:
            if letter in gift_coll[i + 1] and letter in gift_coll[i + 2]:
                common.append(letter)
                # i += 3
                break
    
    for priority in common:
        if priority.isupper():
            priority_sum += (ord(priority) - 38)
        else:
            priority_sum += (ord(priority) - 96)
    print(common)
    print(len(common))
    print(priority_sum)

def compartmentalize(gift_coll):
    common = list()
    priority_sum = 0

    rucksacks = []
    for idx, gift in enumerate(gift_coll):
        gift_len = int(len(gift) / 2)
        rucksacks.append((gift[0:gift_len], gift[gift_len::]))


    for compartments in rucksacks:
        for letter in compartments[0]:
            if letter in compartments[1]:
                common.append(letter)
                break

    for priority in common:
        if priority.isupper():
            priority_sum += (ord(priority) - 38)
        else:
            priority_sum += (ord(priority) - 96)
    
    print(priority_sum)


if __name__ == "__main__":
    gifts = get_input()
    # compartmentalize(gifts)
    elf_groups(gifts)