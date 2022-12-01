#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 18:03:12 2022

@author: rtbec
"""


def main():
    # The highest number of calories carried by an elf
    most_calories = 0
    
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
                most_calories = carried_calories if (carried_calories > most_calories) \
                    else most_calories
                carried_calories = 0
            # add to elf's total
            else:
                carried_calories += int(line.strip())
    
    print(f"The elf with the most Calories is carrying a total of {most_calories} Calories")



if __name__ == "__main__":
    main()