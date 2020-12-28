openclose = input()
dic = {"open": ["(", "["],
       "close": [")", "]"],
       ")": "(",
       "]": "["}


def check():
    stack = []
    for c in openclose:
        if c in dic["open"]:
            stack.append(c)
            continue
        elif stack and c in dic["close"]:
            counter = dic[c]
            val = stack.pop()
        else:
            return 0

        if val == counter:
            result = 2 if val == "(" else 3
            stack.append(result)
        elif isinstance(val, int):
            total = 0
            while stack and isinstance(val, int):
                total += val
                val = stack.pop()
            if val == counter:
                total *= 2 if val == "(" else 3
            else:
                return 0
            stack.append(total)
        else:
            return 0

    result = 0
    while stack:
        val = stack.pop()
        if not isinstance(val, int):
            return 0
        result += val
    return result


print(check())
