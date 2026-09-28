class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Same as the previous 3Sum Problem
            -> 3 Pointers
        """
        def classic_3pointers():
            """
            Similar implementation to the previous 3Sum problem
                Space: O(1)
                Time: O(n^2)
            Since it's sorted:
                min_val will always be: nums[0] + nums[1] + nums[2]
                max_val will always be: nums[-1] + nums[-2] + nums[-3]
                    If min_val > target:
                        -> return min_val
                    elif max_val < target:
                        -> return max_val
            """
            nums.sort()
            l = len(nums)

            min_val = nums[0] + nums[1] + nums[2]
            max_val = nums[-1] + nums[-2] + nums[-3]
            if min_val > target:
                return min_val
            if max_val < target:
                return max_val

            print(nums)

            best_total = 0
            best_rem = 10e10
            for i in range(l - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, l - 1
                while left < right:
                    #print(f"curr, left, right = {nums[i]}, {nums[left]}, {nums[right]}")
                    total = nums[left] + nums[right] + nums[i]
                    remainder = total - target
                    #print(f"Total: {total} | Remainder: {abs(remainder)}")
                    #print(f"Best Remainder: {best_rem} | Best Total: {best_total}")
                    #print(f"-"*59)

                    if abs(remainder) < best_rem:
                        best_rem = abs(remainder)
                        best_total = total

                    if remainder == 0:
                        return total
                    elif remainder > 0:
                        right -= 1
                    else:
                        left += 1
            return best_total

        return classic_3pointers()
        