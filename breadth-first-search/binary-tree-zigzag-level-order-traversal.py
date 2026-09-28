# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        def bfs(root):
            out = []
            queue = [root]
            level = 0
            while queue:
                level_lst = []
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if node is None:
                        continue
                    if level % 2 != 0:
                        level_lst.insert(0, node.val)
                    else:
                        level_lst.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

                if len(level_lst) > 0:
                    out.append(level_lst)
                level += 1
            return out
        return bfs(root)