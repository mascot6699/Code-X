class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operator = {
            "+" : lambda y, x : x + y,
            "-" : lambda y, x : x - y,
            "*" : lambda y, x : x * y,
            "/" : lambda y, x : int(float(x) / y), # special care needed here (6/-132) = -1 but 6.0/-132 = 0 :)
        }
        stack = []
        for x in tokens:
            if x in operator:
                stack.append(operator[x](stack.pop(), stack.pop()))
            else:
                stack.append(int(x))
        return stack[0]
