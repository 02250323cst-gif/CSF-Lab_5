def is_balanced(expr):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}

    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pairs[ch]:
                return "Not Balanced"

    if not stack:
        return "Balanced"
    return "Not Balanced"

# TEST
print(is_balanced("(a+b)*(c+d)"))
print(is_balanced("(a+b)*(c+d"))