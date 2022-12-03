#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 18:32:39 2022

@author: rtbec
"""

# 1 - rock
# 2 - paper
# 3 - scissors
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
            
    print(f"With the strategy guide, I should end with a total score of {total_score}")


if __name__ == "__main__":
    part1()