# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Intuition:
            Gotta log the ancestors of each node
                Because there's no way to actually know unless you log it
            i.e: root = [5,3,8,1,4,7,9,null,2], p = 1, q = 9
                When you reach 1, the ancestors of 1 should be a list that includes:
                    [5, 3, 1]
                When you reach 9, the ancestors of 9 should be:
                    [5, 8, 9]
                Then we take the min of the intersection

            i.e: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
                3 ancestors: [5, 3]
                4 ancestors: [5, 3, 4]
        """

        def get_ancestors(
            root: TreeNode,
            target_node: TreeNode,
            ancestor_lst: list[TreeNode] = []):
            """ 
            We gotta implement backtracking since we're saving
                the trees inside a list
            If go left doesnt work -> we pop that root and go right

            ORRRR, we can just create a copy of ancestor_lst
                and make it so each list is independent of each other
            """
    
            if root is None:
                return None

            ancestor_lst.append(root)
            if root == target_node:
                return ancestor_lst

            # search left
            res = get_ancestors(root.left, target_node, ancestor_lst.copy())
            if res is not None:
                return res

            # search right
            res = get_ancestors(root.right, target_node, ancestor_lst.copy())
            return res

        def get_ancestors_improved(
            root: TreeNode,
            target_node: TreeNode,):
            """
            Since this is a binary search tree
                We don't actually have to search every node for target node

            Note:
                Don't put ancestor_lst inside the function parameters
                    Because they will share the same list
                    
                    anc_p = get_ancestors_improved(root, p)
                        -> ancestor_lst has ancestors of p

                     anc_q = get_ancestors_improved(root, q)
                        -> ancestor_lst starts as the ancestors of p
            """
            ancestor_lst = []
            while root != target_node:
                ancestor_lst.append(root)
                if target_node.val > root.val:
                    root = root.right
                elif target_node.val < root.val:
                    root = root.left

            ancestor_lst.append(root)
            return ancestor_lst

        anc_p = get_ancestors_improved(root, p)
        anc_q = get_ancestors_improved(root, q)
        print(f"Ancestors of {p.val}/p: {anc_p}")
        print(f"Ancestors of {q.val}/q: {anc_q}")
        
        LCA_node = None
        for node in anc_p:
            if node in set(anc_q):
                # LCA is the NOT the smallest value ancestor
                    # but the LAST to appear
                LCA_node = node

        print(f"Lowest Common Ancestor: {LCA_node}")
        return LCA_node