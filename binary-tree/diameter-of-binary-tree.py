# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Basically the Longest Straight Path

        Intuition:
            Breaking it down to subproblems

                The Longest Path passes through any single node is:
                    path_left + path_right // could also be the diameter
        
                The longest single path starting from any node is:
                    1 + max(path_left, path_right)
                Since we cannot turn back once we've went down either left or right
                    -> the limiting factor is the length of each path
                    -> Pick the longest every time

        In the example
              1
            2   3
          4   5

          The longest path that passes through 1 is: 4 -> 2 -> 1 -> 3
                                                        OR
                                                    5 -> 2 -> 1 -> 3
            => The longest path that passes through 1
                is the longest path to its left and right
                -> Longest path that passes through 2 and 3

        The longest path that pass through 2 is 4 -> 2 (left) or 5 -> 2 (right)
            Since we can only one path, either going 4 -> 2 or 5 -> 2, we gotta do:
                max(left_path, right_path)
        
        Similarly for 3, since 3.left and 3.right is None, it returns 0 for both left and right
        """

        longest_path = 0
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            cnt_left = dfs(node.left)
            cnt_right = dfs(node.right)

            nonlocal longest_path
            longest_path = max(longest_path, cnt_left + cnt_right)

            return 1 + max(cnt_left, cnt_right)
        dfs(root)
        return longest_path
        