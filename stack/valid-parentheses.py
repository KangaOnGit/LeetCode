class Solution:
    def isValid(self, s: str) -> bool:
        """
            Stack
        Intuition:
            Whenever there's a question that requires "pairs", you use stack
        """
        close_bracket = [")", "}", "]"]
        open_bracket = ["(", "{", "["]
        if s[0] in close_bracket or s[-1] in open_bracket:
            return False

        stack = []
        for char in s:
            if len(stack) >= 1 and ((stack[-1], char) in zip(open_bracket, close_bracket)):
                # Remove the Pair
                stack.pop()
            else:
                # Append if not Pair
                stack.append(char)

        return len(stack) == 0