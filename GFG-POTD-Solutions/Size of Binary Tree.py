class Solution:
    def getSize(self, root):
        if root is None:
            return 0
        return 1 + self.getSize(root.left) + self.getSize(root.right)