class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def brute_force():
            """
            Time Complexity: O(N^2), Space Complexity: O(1)
            Loop though each element, take minimum height -> Height of Container
            """
            max_area = 0
            for i in range(len(height)):
                for j in range(1, len(height)):
                    min_height = min(height[j], height[i])
                    area = min_height*(j-i)
                    if area > max_area:
                        max_area = area
            return max_area

        def two_pointer():
            """
            Preliminary Idea:
                1 Pointer at the Start (i), 1 Pointer at the End (j)
                if height[i] < height[j] then we increment i by 1, else decrement j by 1
                BUT, how to justify the above statement?
            The WIDTH of the container will ALWAYS decrease whether we move i or j.

                Width = Left-Right
                if we increment i then Right = i + 1
                    -> Width = Left - Right - 1
                if we increment j then Left = j - 1
                    -> Width = Left - 1 - Right

                ===> Width is NOT the limiting factor, it's the height.
                        Therefore, we must try to increase the limiting height
            """
            max_area = 0
            left = 0
            right = len(height) - 1
            while left < right:
                width = right - left
                if height[left] <= height[right]:
                    ht = height[left]
                    left +=1
                else:
                    ht = height[right]
                    right -= 1
                area = width*ht
                max_area = max(area, max_area)
            return max_area

        return two_pointer()