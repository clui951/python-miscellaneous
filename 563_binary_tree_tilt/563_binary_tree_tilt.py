# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS search to find sum of subtrees
    # after getting sums of both the node's children, calculate the tilt of the current node
    # add that to a global count
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        treeTilt = self.findTiltDfs(root)[1]
        return treeTilt

    # returns sum and tilt of tree rooted at curr
    def findTiltDfs(self, curr):
        if curr == None:
            return 0,0

        leftSum, leftTreeTilt = self.findTiltDfs(curr.left)
        rightSum, rightTreeTilt = self.findTiltDfs(curr.right)

        treeSum = curr.val + leftSum + rightSum
        treeTilt = abs(leftSum - rightSum) + leftTreeTilt + rightTreeTilt
        
        return treeSum, treeTilt


    # Same idea as above, but if we were to use nonlocal such that each Dfs call can update value
    def findTilt2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        totalTreeTilt = 0

        # returns sum of tree starting at curr, while updating treeTilt parent value
        def findTiltDfs2(curr):
            nonlocal totalTreeTilt
            
            if curr == None:
                return 0

            leftSum = findTiltDfs2(curr.left)
            rightSum = findTiltDfs2(curr.right)

            treeSum = curr.val + leftSum + rightSum
            totalTreeTilt += abs(leftSum - rightSum)
            
            return treeSum
        
        findTiltDfs2(root)
        return totalTreeTilt





if __name__ == "__main__":
    print("=== findTilt ===")

    # build test tree
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    assert Solution().findTilt(t1) == 1
    assert Solution().findTilt2(t1) == 1

    print("=== done! ===")