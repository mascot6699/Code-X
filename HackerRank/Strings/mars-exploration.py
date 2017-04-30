#!/bin/python3
import sys
from collections import Counter
S = input().strip()
print(len(S) - (Counter(S[::3])['S']+Counter(S[1::3])['O']+Counter(S[2::3])['S']))

