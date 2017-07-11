# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        L = [root]
        result = []
        while len(L) > 0:
            length = len(L)
            N = 0
            for i in range(length):
                node = L.pop(0)
                N = N + node.val
                if node.left:
                    L.append(node.left)
                if node.right:
                    L.append(node.right)
            result.append(float(N)/length)
        return result
            
            
            