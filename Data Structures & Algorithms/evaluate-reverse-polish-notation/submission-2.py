class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(eval(f"{a}{token}{b}")))
            else:
                stack.append(int(token))
        return stack[0]
