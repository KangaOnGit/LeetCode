class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Is this 3Sum but with 4 fucking pointers?
        """

        nums.sort()
        print(f"Sorted: {nums}")
        def pointers():
            res = []
            for i in range(len(nums) - 3):
                if nums[i] > target and target >= 0:
                    break
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                for j in range(i+1, len(nums) - 2):
                    if nums[j] + nums[i] > target and target >= 0:
                        continue
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue
                    left, right = j+1, len(nums) - 1
                    while left < right:
                        #print(f"i, j, l, r = {i}, {j}, {left}, {right}")
                        #print(f"i, j, l, r = {nums[i]}, {nums[j]}, {nums[left]}, {nums[right]}")
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        #print(f"Total: {total} | Target: {target}")
                        if total == target:
                            res.append([nums[i], nums[left], nums[right], nums[j]])
                            left += 1
                            while left < right and nums[left] == nums[left - 1]:
                                #print(f"nums[left]/{left}: {nums[left]}")
                                #print(f"nums[left-1]/{left-1}: {nums[left-1]}")
                                left += 1
                        elif total - target > 0:
                            #print(f"Total - Target: {total - target}")
                            right -= 1
                        else:
                            #print(f"Total - Target: {total - target}")
                            left += 1
                        #print(f"-"*59)
            return res
        return pointers()
