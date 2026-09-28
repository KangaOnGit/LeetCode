class MinStack:
    def __init__(self):
        """
        Space: O(n + m) -> O(n) (Still Constant)
        """
        self.stack = [] # O(n)
        self.min_stack = [] # O(m)

    def push(self, val):
        self.stack.append(val)
        
        # If Empty or val is smaller than prev min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]