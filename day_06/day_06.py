#!/usr/bin/env python3

import sys

file_in = "input2.txt"

def get_input():
    with open(file_in) as fi:
        signal = fi.read()
    return signal
    # print(signal)

def find_packet(signal):
    for idx in range(len(signal) - 4):
        unique_chars = set(signal[idx: idx + 4])
        if len(unique_chars) == 4:
            first_marker = idx + 4
            break

    print(unique_chars)
    print(first_marker)

def find_longer_packet(signal):
    for idx in range(len(signal) - 14):
        unique_chars = set(signal[idx: idx + 14])
        if len(unique_chars) == 14:
            first_marker = idx + 14
            break

    print(unique_chars)
    print(first_marker)
    pass

# Main body
if __name__ == '__main__':
    signal = get_input()
    # find_packet(signal)
    find_longer_packet(signal)

