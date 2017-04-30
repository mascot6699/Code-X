from collections import Counter
import string
str1 = input().lower().replace(' ', '')
print("pangram") if len(Counter(str1).keys()) == 26 else print("not pangram")
