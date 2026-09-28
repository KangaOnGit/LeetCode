class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Similar to
            "Find Min in Rotated Sorted Array"
        Overview:
            Since it's sorted, there will always be a lower-half and an upper-half
            The inflection point is at n == len(nums)//2 where it can take the form:
                [3, 4, 5, 6, 1, 2]
                Where the lower values are on the unrotated "upper-half"
                If n < len(nums)//2, the lower values are on the lower-half
                    They haven't fully migrated

        Problem:
            Not applied to this problem
            [3, 4, 5, 6, 1, 2]
                If use same algo and target = 3
                it will make left = 3 (index)
            The reason the other algo worked is because it's finding the minimum values
            And for that minimum value, at n == len(nums)//2
                It will be at the unrotated "upper-half"//near the end of the list

        Solution:
            There will always be one half that's sorted if you rotate the array
            The rotation will break the equilibrium that there's 2 sorted halves
                and make it so there's only 1 at a time
                    -> Check if the target is in range
                        -> If not in range then it's in the other half thats not sorted
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1