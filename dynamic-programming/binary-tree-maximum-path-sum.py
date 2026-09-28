# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """ 
        Similar Code to the "Diameter of a Binary Tree"
            Where you evaluate the Straight Path
                (No turn-around)

        You start with a Root Node
            You evaluate its left and right
            in Diameter, you pick the route with the higher number of nodes
            similarly, you pick the route with the higher total value

            Diameter:
                Left Route number of nodes = cnt_left + 1 (1 is the root Node)
                Right Route number of nodes = cnt_right + 1 (1 is the root Node)

            For this, it's
                Left Route Sum = cnt_left + root.val
                Right Route Sum = cnt_right + root.val
            
            Small Twist:
                Max Nodes in "Diameter of Binary Tree" is:
                    max_nodes = max(max_nodes, cnt_left + cnt_right + 1)
                    You take the Root Node, you sum its left and right path and itself (1)
                        and you evaluate it with other max_nodes
                
                Max Path, however, is:
                    max_path = max(max_path,
                    cnt_left + cnt_right + root.val,
                    root.val,
                    cnt_left + root.val,
                    cnt_right + root.val)
                    You still take the Root Node and sum its left and right total and itself (root.val)
                    But now, since there are negative values,
                        The largest path is either:
                            Itself
                            Itself + its left + its right
                            Itself + its right
                            Itself + its left
                            other max_paths/its other selfs

        
        It's a matter of breaking problems into smaller subproblems
        """
        

        max_path = float("-inf")
        def dfs(root: TreeNode):
            if not root:
                return 0

            cnt_left = dfs(root.left)
            cnt_right = dfs(root.right)

            nonlocal max_path
            max_path = max(max_path,
            root.val + cnt_left + cnt_right,
            root.val,
            root.val + cnt_left,
            root.val + cnt_right)

            return max(root.val + max(cnt_left, cnt_right), root.val)
        dfs(root)
        return max_path