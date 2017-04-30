str1 = input() 
stack = []
stack_len = -1
for char in str1:
    # print(stack)
    if stack_len == -1 or stack[stack_len] != char:
        stack.append(char)
        stack_len += 1
    else:
        stack.pop()
        stack_len-=1
        
print("".join(stack)) if len(stack) != 0 else print('Empty String')
