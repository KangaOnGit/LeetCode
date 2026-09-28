class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        O(1) Constant Space -> No Dictionary for Lookup
        Approach:
            Rather than Dict Lookup
                Lookup directly inside the list -> O(n) Time
            Sorted in an Increasing Order (Non-Decreasing)
                => Think right away to 2 Pointers
                        1 Pointer at Start, 1 at End
                        if sum(2 pointers) > target 
                            => Move End pointer back by 1
                            Else Move Start pointer up by 1
        """

        def two_loops():
            """
            Worst Case Time Complexity: O(n^2)
            Space: O(1)
            """
            for i in range(len(numbers) - 1):
                rem = target - numbers[i]
                for j in range(i + 1, len(numbers)):
                    if numbers[j] == rem:
                        return [i + 1, j + 1]
        #return two_loops()

        def two_pointers():
            l = 0
            r = len(numbers) - 1
            while l < r:
                totes = numbers[l] + numbers[r]
                if totes == target:
                    return [l + 1, r + 1]
                elif totes > target:
                    r -= 1
                else: 
                    l += 1
        return two_pointers()