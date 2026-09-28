# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Preorder: Root -> Left Root of Left SubTree -> Right Root of Right SubTree
        Inorder: Left -> Root -> Right (by depth/left-most)

        Then:
            Preorder gives the Root Node for each SubTree
            Inorder gives the Left and Right of each Node
        
        Intuition:
            Inorder goes from Left -> Middle/Root -> Right
            -> We could find out which nodes sits to the Left and Right
                Of the Middle Node using the Inorder List
            I.e: Inorder [9, 3, 15, 20, 7]
                 Preorder: [3, 9, 20, 15, 7]
                Loop through Preorder, sees 3
                Finds 3 in Inorder, looks Left and Right
                    => 9 is Left of 3 and [15, 20, 7] is Right of 3
                    Since [15, 20, 7] is Right of 3
                    We can find which one is the 1st to the Right
                        by using the Preorder List
                        Since it goes level-by-level (BFS)
                        The first to appear is the Right
        Example:
        Preorder: [3, 9, 20, 6, 8, 15, 7]
        Inorder: [6, 9, 8, 3, 15, 20, 7]
                            3
                        9       20
                    6     8   15    7
        Inorder gives Length of Left-Right Tree, Preorder gives Level
        Another way to think about:
            We can break it into subproblems
            Rather than finding 9 and 20 to assign to 3 and then finding 6, 18, 15, 7
                to assign to 9 and 20
            => We can create the tree [9, 6, 8] and assign it to 3
            => Create Left and Right Tree then assign it to middle/Root

        Another way to think about:
            Rather than the previous subproblems where it's bottom-up
            We can do top-down by building Left Tree First then building Right Tree
            Find 3 -> Find Left and Right Nodes
            From Left, find the Left that binds to 3 then append it
                From that Left, if theres more nodes, complete it
        """

        def own_sol(
                preorder_idx: int,
                nodes_lst: list[int] = None,
                left_bound: int = 0,
                right_bound: int = None):
                """
                Made from the Intuition and Examples from above ^^

                If there's a pre-existing Left/Right List of Nodes:
                    Loop through Preorder to find the node that belongs to that List
                        (First Occurence since no Dupes)
                        If found, create a Tree with that Node
                        Get its Index
                else:
                    (First Case where we get the Root Node of Entire Tree)
                
                After getting the Node Idx
                list of left nodes = inorder[left_bound:idx]
                list of right nodes = inorder[idx + 1:right_bound]

                If right_list exists:
                    Build Right Tree and Left Tree
                        Right Tree has left_bound = idx + 1
                                        right_bound = len(inorder)
                        curr_node.right = right_tree # At the most-base level, assign leaf node
                        
                if left_list exists:
                        Left Tree has right_bound = idx
                                        left_bound = 
                        curr_node.left = left_tree # At the most-base level, assign leaf node
            
                If one of 2 list doesn't exist
                    -> We've arrived at the base case where it's a leaf node
                    return that leaf node
                """
                if right_bound is None:
                    right_bound = len(inorder)

                # Find the root in this subtree
                if nodes_lst is not None:
                    for idx in range(preorder_idx, len(preorder)):
                        if preorder[idx] in nodes_lst:
                            root_preorder_idx = idx # Preorder index
                            root_idx = inorder.index(preorder[idx]) # Inorder index
                            curr_root = TreeNode(preorder[idx])
                            break
                else:
                    # Added solely for the 1st Case
                    root_preorder_idx = preorder_idx
                    root_idx = inorder.index(preorder[preorder_idx])
                    curr_root = TreeNode(preorder[preorder_idx])

                # Nodes to the left/right of root in inorder
                left_lst = inorder[left_bound:root_idx]
                right_lst = inorder[root_idx + 1:right_bound]

                # Build left subtree
                if left_lst:
                    left_tree, next_preorder_idx = own_sol(
                        preorder_idx=root_preorder_idx + 1,
                        nodes_lst=left_lst,
                        left_bound=left_bound,
                        right_bound=root_idx
                    )
                    curr_root.left = left_tree
                else:
                    # Skip over all the Index of Nodes belong to Left Subtree
                    next_preorder_idx = root_preorder_idx + 1

                # Build right subtree
                if right_lst:
                    right_tree, next_preorder_idx = own_sol(
                        preorder_idx=next_preorder_idx,
                        nodes_lst=right_lst,
                        left_bound=root_idx + 1,
                        right_bound=right_bound
                    )
                    curr_root.right = right_tree

                return curr_root, next_preorder_idx

        #return own_sol(0)[0]

        inorder_idx = {
            value: idx
            for idx, value in enumerate(inorder)
        }
        preorder_idx = 0
        def better_sol(left_bound, right_bound):
            """
            Basically my solution but way cleaner

            Rather than passing preorder_idx,
                Since we gonna build left subtree then right subtree
                just make it a nonlocal variable

            Rather than looping, just make a dictionary for faster search

            Rather than creating left and right lists,
                We can just save the left and right bound
                    which is the start-end of the left and right lists

                If left bound > right bound then thats a leaf node
                    return None
            Subproblems:
                            3
                        9       20
                    6     8   15    7

            At leaf node 6, left > right bound so both 6.left and 6.right is None
            Tree 6 is built -> Calls back to 9, append the Tree 6 to 9.left
            Similarly to 8...
            """
            nonlocal preorder_idx

            # No nodes in this subtree
            if left_bound > right_bound:
                return None

            # Preorder gives us the root
            root_value = preorder[preorder_idx]
            preorder_idx += 1

            root_idx = inorder_idx[root_value]

            root = TreeNode(root_value)

            # Everything left of root in inorder
            # belongs to the left subtree
            root.left = better_sol(left_bound, root_idx - 1)

            # Everything right of root in inorder
            # belongs to the right subtree
            root.right = better_sol(root_idx + 1, right_bound)

            return root

        return better_sol(0, len(inorder) - 1)