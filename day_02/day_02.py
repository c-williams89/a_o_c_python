#!/usr/bin/python3

input_file = "input.txt"
def read_input():
    with open(input_file) as file_in:
        strategy = file_in.read().splitlines()
    return strategy

def calc_hand(strategy):
    score = 0
    draw = 3
    win = 6
    loss = 0
    lose_game = []
    rock_score = 1
    draw_game = []
    paper_score = 2
    win_game = []
    scissor_score = 3

    for hand in strategy:
        if hand[2] == 'X':
            lose_game.append(hand)
        elif hand[2] == 'Y':
            draw_game.append(hand)
        elif hand[2] == 'Z':
            win_game.append(hand)
    
    for game in lose_game:
        if game[0] == 'A':
            score += (scissor_score + loss)
        if game[0] == 'B':
            score += (rock_score + loss)
        if game[0] == 'C':
            score += (paper_score + loss)

    for game in win_game:
        if game[0] == 'A':
            score += (paper_score + win)
        if game[0] == 'B':
            score += (scissor_score + win)
        if game[0] == 'C':
            score += (rock_score + win)

    for game in draw_game:
        if game[0] == 'A':
            score += (rock_score + draw)
        if game[0] == 'B':
            score += (paper_score + draw)
        if game[0] == 'C':
            score += (scissor_score + draw)
    print(score)

def calc_score(strategy):
    score = 0
    draw = 3
    win = 6
    loss = 0
    rock = []
    rock_score = 1
    paper = []
    paper_score = 2
    scissor = []
    scissor_score = 3

    for hand in strategy:
        if hand[2] == 'X':
            rock.append(hand)
        elif hand[2] == 'Y':
            paper.append(hand)
        elif hand[2] == 'Z':
            scissor.append(hand)
    
    for game in rock:
        if game[0] == 'A':
            score += (rock_score + draw)
        if game[0] == 'B':
            score += (rock_score + loss)
        if game[0] == 'C':
            score += (rock_score + win)

    for game in paper:
        if game[0] == 'A':
            score += (paper_score + win)
        if game[0] == 'B':
            score += (paper_score + draw)
        if game[0] == 'C':
            score += (paper_score + loss)

    for game in scissor:
        if game[0] == 'A':
            score += (scissor_score + loss)
        if game[0] == 'B':
            score += (scissor_score + win)
        if game[0] == 'C':
            score += (scissor_score + draw)
        
    print(score)

if __name__ == "__main__":
    strategy = read_input()
    calc_score(strategy)
    calc_hand(strategy)