#!/bin/python3

import sys

def is_hr_present(string):
    hackerrank = "hackerrank"
    i = 0
    for j in range(len(string)):
        if hackerrank[i] == string[j] and i < 9:
            i+=1
            j+=1
    return "YES" if i == 9 else "NO"

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    print(is_hr_present(s))

