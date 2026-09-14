class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        _open = set(['[', '{', '('])
        _close = set([']', '}', ')'])

        for bracket in s:
            if bracket in _open:
                stack.append(bracket)

            if bracket in _close:
                if not stack:
                    return False 

                if bracket == '}' and stack[-1] == '{' or bracket == ')' and stack[-1] == '(' or bracket == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False


        if stack:
            return False
        else:
            return True

        