#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:03:12 2022

@author: rtbec
"""

import numpy as np

def part1():
    # The highest number of calories carried by an elf
    most_calories = 0
    
    with open("input.txt", "r") as f:
        # The total calories between each item the current elf is carrying
        carried_calories = 0
        for line in f:
            # end of elf's bag
            if line == "\n":
                most_calories = carried_calories if (carried_calories > most_calories) \
                    else most_calories
                carried_calories = 0
            # add to elf's total
            else:
                carried_calories += int(line.strip())
    
    print(f"The elf with the most Calories is carrying a total of {most_calories} Calories")


def part2():
    # The top 3 highest number of calories carried by elves
    most_calories = np.zeros(3, dtype=int)
    print(most_calories)
    
    with open("input.txt", "r") as f:
        # The total calories between each item the current elf is carrying
        carried_calories = 0
        ln = 0
        for line in f:
            ln += 1
            # end of elf's bag
            if line == "\n":
                # sanity check
                # if (carried_calories > most_calories): 
                #     print(ln, carried_calories)
                # most_calories = carried_calories if (carried_calories > most_calories) \
                    # else most_calories
                if carried_calories > min(most_calories):
                    most_calories[np.argmin(most_calories)] = carried_calories
                    
                carried_calories = 0
            # add to elf's total
            else:
                carried_calories += int(line.strip())
    
    print(f"Calories carried by the top 3 elves: {most_calories}")
    print("The top 3 elves with the most Calories are carrying a total of "
              f"{np.sum(most_calories)} Calories")


if __name__ == "__main__":
    part1()
    part2()