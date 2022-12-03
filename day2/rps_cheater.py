#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:32:39 2022

@author: rtbec
"""

# 1 - rock / loss
# 2 - paper / draw
# 3 - scissors / win
cypher = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3
    }

def part1():
    total_score = 0
    
    with open("input.txt", "r") as f:
        
        for line in f:
            # converts the line into the numeric values for each move
            o_move, s_move = [cypher[move] for move in line.split()]
            
            # add the base value of the move
            total_score += s_move
            
            # Add points on win / draw
            # win on 1 2, 2 3, 3 1
            if (o_move + 1) % 3 == (s_move % 3):
                total_score += 6
            elif o_move == s_move:
                total_score += 3
            
    print(f"Using the strategy guide wrong, I should end with a total score of {total_score}")
    
    
    
def part2():
    total_score = 0
    # Using a dictionary is the cleanest way I could think of
    win_dict = {1: 2, 2: 3, 3: 1}
    loss_dict = {1: 3, 2: 1, 3: 2}
    
    with open("input.txt", "r") as f:
        
        for line in f:
            # converts the line into the numeric values for each move
            o_move, result = [cypher[move] for move in line.split()]
            
            if result == 1:
                total_score += loss_dict[o_move]
            elif result == 2:
                total_score += o_move + 3
            elif result == 3:
                total_score += win_dict[o_move] + 6
            
            
    print(f"Using the strategy guide correctly, I should end with a total score of {total_score}")


if __name__ == "__main__":
    part1()
    part2()