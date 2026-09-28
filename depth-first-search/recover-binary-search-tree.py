# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def linear_space(root):
            """
            dfs for a BST is strictly increasing
                -> Returned List should be in Increasing Order (Similar to InOrder Traversa)
                -> If not, we sort it
            -> The Sorted List will be the Recovered BST
            -> DFS/InOrder Traversal of a BST will return a SORTED LIST
            I.e:
                3
               / \
             1    4
                 /              
                2
            returned list: 1 -> 3 -> 2 -> 4
            sorted list: 1 -> 2 -> 3 -> 4 == Recovered List
            returned_list[i] = sorted_list[i]
                    -> 1 -> 2 -> 3 -> 4
            """
            tmp = []
            def dfs(node):
                if not node:
                    return
                dfs(node.left)
                tmp.append(node)
                dfs(node.right)

            dfs(root)
            srt = sorted(node.val for node in tmp)
            for i in range(len(srt)):
                tmp[i].val = srt[i]
        #linear_space(root)

        def const_space(root):
            """
                To do in-place modification of a Tree
                    You just get its node... and change it directly...
            """
            prev, first_to_swap, last_swap = None, None, None
            def inOrder_traversal(root):
                """
                    Inorder traversal goes left tree then right tree then to root
                    in BST, it's strictly increasing -> Previous Value must be smaller than Current Value
                If Current Value <= Previous Value:
                    Remember those 2 Nodes to swap
                Note: We swap the first node that needs swapping
                            with the LAST NODE that needs swapping
                """
                if not root:
                    return
                nonlocal prev
                nonlocal first_to_swap
                nonlocal last_swap
                # Do left Tree
                inOrder_traversal(root.left)
                if prev is not None and root.val <= prev.val:
                    if first_to_swap is None:
                        # Remember the First Error/Swap
                        first_to_swap = prev
                    # Get the Latest Error/Swap
                    last_swap = root
                # Save previous node
                prev = root
                # Do Right Tree
                inOrder_traversal(root.right)
            inOrder_traversal(root)
            last_swap.val, first_to_swap.val = first_to_swap.val, last_swap.val
        const_space(root)