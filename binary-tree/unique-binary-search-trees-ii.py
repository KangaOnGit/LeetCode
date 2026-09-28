# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        Binary Search Tree:
            Left Node < Root Node
            Right Node > Root Node
        
        For every number from 1 -> n:
            We can either choose that number as the root or we don't
                        Note: But we still HAVE to use ALL NUMBERS from 1 -> n
                                -> kinda similar to Backtracking
            Then the Left Tree will be every number from 1 -> number (Smaller than number)
                     Right Tree will be every number from number + 1 -> n (Larger than number)
        """

        def generate(left, right):
            """
                Generate Left and Right Subtree from Root Tree
            """
            if left > right:
                # No Left Tree
                return [None]

            res = []
            for num in range(left, right + 1):
                for left_tree in generate(left, num - 1):
                    for right_tree in generate(num + 1, right):
                        root = TreeNode(num, left_tree, right_tree)
                        res.append(root)
            return res

        cache = {}
        def generate_memoization(left, right, cache):
            if left > right:
                # No Left Tree
                return [None]

            # If the solution to this (left, right) already appears
            if (left, right) in cache:
                return cache[(left, right)]

            res = []
            for num in range(left, right + 1):
                for left_tree in generate_memoization(left, num - 1, cache):
                    for right_tree in generate_memoization(num + 1, right, cache):
                        root = TreeNode(num, left_tree, right_tree)
                        res.append(root)

            # Log all possible solutions of (left, right)
            cache[(left, right)] = res

            return cache[(left, right)]

        return generate_memoization(1, n, cache)