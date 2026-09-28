# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Intuition:
            False if abs(path_left - path_right) > 1 else True

            We gotta take the longest path for path_left
                and subtract it with the longest path_right
            
            the longest path_left/path_right will be the max(path_to_its_left,
                                                             path_to_its_right)
        
            Split in multiple Subproblems for longest path_left and path_right
                1
            2       3
                4       6
              5

            The longest path_left of 1 is equal to the longest path of 3
                the longest path of 3 is either its left path
                            5 -> 4 -> 3
                    or its right path
                            6 -> 3
                => max(right_path, left_path)
        """
        res = True
        
        def dfs(root, cnt):
            if not root:
                return cnt - 1

            # Compute Left and Right Path Length
            cnt_left = dfs(root.left, cnt + 1)
            cnt_right = dfs(root.right, cnt + 1)
    
            nonlocal res
            if abs(cnt_left - cnt_right) > 1:
                res = False

            # Return the Longest Path
            return max(cnt_left, cnt_right)
        dfs(root, 0)
        return res