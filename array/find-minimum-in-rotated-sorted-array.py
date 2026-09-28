class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        It seems that the "rotation" is just moving the elements
            n-index

        We don't know how many times it's been rotated
            If we try to find how many times it's been rotated
                then we must know the min/max of nums
                which requires an O(n) Search

        We want O(logn) -> Binary Search
            -> We don't actually need to know how many times it's been rotated
            -> We just need to figure out WHICH HALF contains the minimum


        Intuition:
            Although the Array is Rotated, there's still a clear boundary
                between Upper and Lower
            That means, the array is still divided into the lower-half and upper-half
                                                                (Sorted Regions)

            We find the middle value, check left and right of middle
                whichever side has a smaller value -> check that side
                if both side has larger value than middle -> that's the smallest possible value
        
        There are cases where the smallest value might be on the side that's "larger"
            [2, 3, 4, 5, 6, 1]
                -> mid = 5, 6 is larger but 1 is also on the same side as 6
                -> can't check neighbours / local information
                -> Have to check global information
                -> Check endpoints of left and right

            if nums[mid] > nums[right] that means
                the rotation n is larger than len(nums)//2
                that means the lower part is already on the right side

            if nums[mid] < nums[right]
                the rotation is less than len(nums)//2
                the larger values haven't finished moving all to the right side

            the opposite for nums[left]
                if nums[mid] < nums[left]
                    the rotation n is less than len(nums)//2
                
                if nums[mid] > nums[left]
                    the rotation n is larger than len(nums//2)
            => We can find out the inflection point of the number of rotation
                by finding if nums[mid] > nums[right] or not
                by finding the inflection point, we also consequently find the half
                    that contains the min value
                
            [6, 1, 2, 3, 4, 5]
                if nums[left] > nums[right] -> we know that its been rotated

        Note: Binary search usually isn't about finding the answer directly.
                It's about finding WHICH HALF can be safely discarded.
        """

        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid # right might be the smallest in of itself
        return nums[left]