class Solution:
    def is_number(self, s: str):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.is_number(token):
                stack.append(int(token))
            else:
                s2 = int(stack.pop())
                s1 = int(stack.pop())

                if token == '+':
                    stack.append(s1 + s2)
                elif token == '-':
                    stack.append(s1 - s2)
                elif token == '/':
                    stack.append(int(s1 / s2))
                else:
                    stack.append(s1 * s2)


        return stack[-1]