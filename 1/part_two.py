#!/usr/local/bin/python3

def solution():
    with open("input.txt") as f:
        input = f.readlines()
        index = 0
        total = 0
        tracker = set()

        while total not in tracker:
            tracker.add(total)
            total += int(input[index])
            index = index + 1 if index < len(input) - 1 else 0
        
        return total

print(solution())