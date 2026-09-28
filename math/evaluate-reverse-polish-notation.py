class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for symbol in tokens:
            if symbol == "+":
                val1 = stack.pop(-2)
                val2 = stack.pop(-1)
                stack.append(int(val1) + int(val2))
            elif symbol == "-":
                val1 = stack.pop(-2)
                val2 = stack.pop(-1)
                stack.append(int(val1) - int(val2))
            elif symbol == "*":
                val1 = stack.pop(-2)
                val2 = stack.pop(-1)
                stack.append(int(val1) * int(val2))
            elif symbol == "/":
                val1 = stack.pop(-2)
                val2 = stack.pop(-1)
                stack.append(int(val1) / int(val2))
            else:
                stack.append(symbol)
        return int(stack[-1])