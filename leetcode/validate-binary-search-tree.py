class Solution:
#if this aint gonna work i am noy gonna do  this question again.
    def inorderchk(self, root, prev):
        if root is not None:
            if not self.inorderchk(root.left, prev):  
                return False

            if prev[0] is not None and root.val <= prev[0].val:  
                return False

            prev[0] = root  
            return self.inorderchk(root.right, prev)  

        return True

    def isValidBST(self, root):
        prev = [None]  
        return self.inorderchk(root, prev)