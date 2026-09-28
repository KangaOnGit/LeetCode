class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic Decreasing Stack
        Intuition:
            - Whenever we see a temperature
                Check if that temperature is larger than recent temperature
                Pop that Recent Temperature
                    Calc number of days by subtracting
                            curr temp idx with recent temp idx
                    Keep popping recent temperature until met larger
        => This way, the stack will always be DECREASING
            => All Recent Elements of Stack will be smaller than or equal to previous elements
            => If found an element that's larger than recent element
                Remove Recent Elements until it's decreasing again
        -> A Stack allows you to do just that, strictly increasing/decreasing
        """
        stack = [] # O(n) Space
        res = [0]*len(temperatures) # O(n) Space
        # Total Space: O(2n) -> O(n)

        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > temperatures[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            else:
                stack.append(idx)
        return res