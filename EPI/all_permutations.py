def all_permutations(elems):
     level = [elems[0]]
     for i in range(1, len(elems)):
         nList = []
         for item in level:
             nList.append(item+elems[i])
             for j in range(len(item)):
                 nList.append(item[0:j] + elems[i] + item[j:])
         level = nList
         # print(level)
      return nList

print(all_permutations("abcde"))

