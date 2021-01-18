def multi_bracket_validation(string: str) -> bool:
    openers = {'{':'}','[':']','(':')'}
    closers = openers.values()
    stack = []

    for c in string:
        if c in openers:
            stack.append(c)
        if c in closers:
            if not stack or c != openers[stack.pop()]:
                return False

    return True if not stack else False