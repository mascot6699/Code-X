symbol_map = {"}":"{", "]" : "[", ")": "("}
def is_matched(expression):
    stack = []
    for symbol in expression:
        # print(stack)
        if symbol in symbol_map.values():
            stack.append(symbol)
        if symbol in symbol_map.keys():
            if len(stack) > 0:
                last_element = stack.pop()
                if symbol_map[symbol] == last_element:
                    pass
                else:
                    return False
            else:
                return False
    if len(stack) != 0:
        return False
    return True
