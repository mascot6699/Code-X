str1 = input() 
b = list(str1)
i = 0
while i < len(b)-1:
    #print(b)
    if b[i] == b[i+1]:
        del b[i]
        del b[i]
        i = 0
        if not len(b):
            print('Empty String')
            break
    else:
        i+=1
print("".join(b))
