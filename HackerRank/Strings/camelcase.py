#!/bin/python3
import sys
input_string = input()
print(len(list(filter(lambda x: (x.isupper() == 1 ), input_string)))+1)
