#!/usr/bin/python3

file_in = "input.txt"

def get_input():
    with open(file_in) as fi:
        clean_pairs = fi.read().splitlines()
    return clean_pairs

def determine_overlap_range(clean_pairs):
    overlap_range = 0
    for pair in clean_pairs:
        print(pair)
        elf_pair = pair.split(',')
        elf_1 = elf_pair[0].split('-')
        elf_2 = elf_pair[1].split('-')
        elf_1_section = []
        elf_2_section = []
        for idx in range(int(elf_1[0]), int(elf_1[1]) + 1):
            elf_1_section.append(idx)
        for idx in range(int(elf_2[0]), int(elf_2[1]) + 1):
            elf_2_section.append(idx)

        for idx in elf_1_section:
            if idx in elf_2_section:
                overlap_range += 1
                break
    print(overlap_range)

def determine_overlap(clean_pairs):
    overlap = 0
    for pair in clean_pairs:
        elf_pair = pair.split(',')
        elf_1 = elf_pair[0].split('-')
        elf_2 = elf_pair[1].split('-')
        if (((int(elf_2[0]) >= int(elf_1[0])) and (int(elf_2[1]) <= int(elf_1[1])))
        or ((int(elf_1[0]) >= int(elf_2[0])) and (int(elf_1[1]) <= int(elf_2[1])))):
            overlap += 1
    print(overlap)

if __name__ == "__main__":
    clean_pairs = get_input()
    determine_overlap(clean_pairs)
    determine_overlap_range(clean_pairs)