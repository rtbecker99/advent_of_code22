#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 13:45:33 2022

@author: rtbec
"""

import string

def map_priorities():
    # loops through lowercase, then upercase letters
    priority_dict = {}
    for counter, letter in enumerate(string.ascii_letters):
        # priorities should start at 1, count starts at 0
        priority_dict[letter] = counter + 1
    
    return priority_dict


def part1(priority_dict):
    priority_sum = 0
    
    with open("input.txt", "r") as f:
        for line in f:
            comp_length = len(line) // 2
            a_comp = set(line[:comp_length])
            b_comp = set(line[comp_length:])

            # feels a little clunky, but needs to convert to a list so I can retrieve
            # the one value from the intersection set
            item = list(a_comp.intersection(b_comp))[0]
            priority_sum += priority_dict[item]
            
            
    print(f"The sum of the priorities for misplaced items is {priority_sum}")
    
    
    
def part2(priority_dict):
    group_priority_sum = 0
    bags = [set(), set(), set()]
    
    with open("input.txt", "r") as f:
        for counter, line in enumerate(f):
            bags[counter % 3] = set(line.strip())

            if counter % 3 == 2:
                # intersection can also be done using & between sets
                item = list(bags[0] & bags[1] & bags[2])[0]
                group_priority_sum += priority_dict[item]
                
            
    print(f"The sum of the priorities for each group's main item is {group_priority_sum}")
    

if __name__ == "__main__":
    priority_dict = map_priorities()
    part1(priority_dict)
    part2(priority_dict)