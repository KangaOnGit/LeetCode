class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Approaches:
            Sorting then Check
                Time Complexity: O(n * logn)

        Turning List into Set -> O(n) Time, worst O(n^2)
        List lookup -> O(n) Time (for ... in list)
        """
        num_dict = set(nums) # O(n) Space and O(n) Time
        def bidirection_one_pass():
            """
                Time : O(n) | O(2n)
                Space Complexity: O(n)
            Potential Work:
                Rather than finding start of sequence
                You can expand both sides of a number
            """
            count = 0
            # O(n) Time
                # Loop through the set
            for num in num_dict:
                cnt = 1 # Count itself

                # Start of sequence
                if num - 1 not in num_dict:
                    while num + 1 in num_dict:
                        num += 1
                        cnt += 1
                count = max(count, cnt)
            return count
        return bidirection_one_pass()
        