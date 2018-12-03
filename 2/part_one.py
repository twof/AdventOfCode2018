#!/usr/local/bin/python3

def solution():
    with open("input.txt") as f:
        input = f.readlines()
        twos = 0
        threes = 0
        
        for line in input:
            histogram = {}
            is_two = False
            is_three = False
            for letter in line:
                if letter in histogram:
                    histogram[letter] += 1
                else:
                    histogram[letter] = 1

            for val in list(histogram.values()):
                if val == 2:
                    is_two = True
                
                if val == 3:
                    is_three = True
            twos += 1 if is_two else 0
            threes += 1 if is_three else 0
 
    print(twos, threes)
    return twos * threes




print(solution())