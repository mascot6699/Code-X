#!/bin/python3
import sys
n = int(input().strip())
s = input().strip()
k = int(input().strip())
lowercase_map = [ chr(ord('a')+(k+x)%26) for x in range(0,26) ]
uppercase_map = [ chr(ord('A')+(k+x)%26) for x in range(0,26) ]
cipher = ""
for char in s:
    if char.islower():
        print(lowercase_map[ord(char)-ord('a')], end="")
    elif char.isupper():
        print(uppercase_map[ord(char)-ord('A')], end="")
    else:
        print(char, end="")
