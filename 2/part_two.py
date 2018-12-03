#!/usr/local/bin/python3

def solution():
    with open("input.txt") as f:
        input = f.readlines()
        
        for linea in input:
            for lineb in input:
                difference_count = 0
                for index in range(0, len(linea) - 1):
                    difference_count += 1 if linea[index] != lineb[index] else 0
                if difference_count == 1:
                    combined = zip(linea, lineb)
                    filtered = filter(lambda tupe: tupe[0] == tupe[1], combined)
                    selected = map(lambda tupe: tupe[0], filtered)
                    return selected
sol = "".join(solution()[:-1])
print(sol)