class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def two_pointers():
            """
            Intuition:
                Similar to the Largest Area of Water Trapped in Container
                Contracting Window
                    Get Min Height in Window
                    Compute Width = num(elements inside Window)
                    Update Area
            Cons:
                [7,1,7,2,2,4]
                -> Expected Output = 8, Code returns 7
                It disregard the fact that Largest Area might
                    not correlated to The Largest Height
                (Unlike in "Largest Area of Water in Container" where
                    Width is guaranteed to Decrease
                    So the Limiting Factor is Height)
            """
            l = 0
            r = len(heights) - 1
            A = 0
            while l <= r:
                min_height = min(heights[l : r + 1])
                w = len(heights[l : r + 1])
                A = max(min_height * w, A)
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1
            return A
        #return two_pointers()

        def another_approach(heights):
            """
            Cases:
                [5, 4, 1, 2] -> 8 (Decreasing Add) | 4*2
                [9, 0] -> 9 (Singular) | 9
                [2,1,5,6,2,3] -> 10 (Increasing Add) | 5*2
            
            Stack:
                        Monotonic Increasing Stack
                -> Trigger something when latest element is smaller

                        Monotonic Decreasing Stack
                -> Trigger something when latest element is larger
            Choose Which? -> Both is Usable, just need the Right Intuition

            Monotonic Increasing Stack:
            [1, 2, 3, 1]: Let's Evaluate [1, 2, 3]
                    The Area are: 1*3, 1*2, 2*2, 3, 2, 1  
                        The Area is shifting Right
                            That means in a Monotonic Increasing Stack
                            The area at an Index = Height at that Index * Number of Columns to its Right
                                (Similar to taking the SMALLEST HEIGHT and MULTIPLYING by the Width)
            [3, 2, 1, 4]
                    Similarly
                        The Area is Shifting LEFT
                            The Area in an Index = Height at that Index * Number of Columns to its Left
            
            """
            A = 0
            s = []
            heights = [0] + heights + [0] # To Avoid NOT having a Boundary

            for right_boundary, h in enumerate(heights):
                if s:
                    # Monotonic Increasing Stack
                        # --> Current bar is the FIRST smaller bar to the right
                            # of every popped bar
                    while h < heights[s[-1]]:
                        # Look to the Right
                        index = s.pop()

                        # [0, 5, 4, 1, 2, 0] Padded
                            # Stack = [0, 2, 3] -> [0, 4, 1]
                                # Left Boundary has Index 0 and we KNOW
                                    # That Between Index 0 -> 2
                                        # there exist bars that are larger than 4
                        left_boundary = s[-1]

                        height = heights[index]
                        width = right_boundary - left_boundary - 1
                        A = max(A, height*width)
                s.append(right_boundary)
            return A
        return another_approach(heights)