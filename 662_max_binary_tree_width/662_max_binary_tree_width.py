class TreeNode:
    left = None
    right = None
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Solution:
    """
        Track each node's depth and position relative to most left of that depth
            At each step, the position will double (because the number of nodes before it will double), and plus one for right child
        Width at a depth will be right most position minus left most position

        
        Option 1: BFS, and the first seen of that height is left most, last seen of certain height is right most
        Option 2: DFS, dict tracks depth -> (leftmost, rightmost) and update max_width as you go
    """
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        width_tracker = {}

        def widthDFSHelper(root, height, position):
            if not root:
                return

            if height not in width_tracker:
                width_tracker[height] = [position, position]
            else:
                if position < width_tracker[height][0]:
                    width_tracker[height][0] = position
                if position > width_tracker[height][1]:
                    width_tracker[height][1] = position

            widthDFSHelper(root.left, height + 1, position * 2)
            widthDFSHelper(root.right, height + 1, position * 2 + 1)

        widthDFSHelper(root, 0, 0)
        max_so_far = 0
        for height in width_tracker:
            low, high = width_tracker[height]
            # print(height, low, high)
            curr_max = high - low + 1
            if curr_max > max_so_far:
                max_so_far = curr_max

        # print(max_so_far)
        return max_so_far
        


    # def widthOfBinaryTree2(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if not root.left and not root.right:
    #         return 1

    #     # dict of depth -> (leftmost_skew, rightmost_skew)
    #     width_tracker = {}
    #     max_skew = 1

    #     def widthDFSHelper(root, height, skew):
    #         nonlocal max_skew

    #         if not root:
    #             return
            
    #         if height not in width_tracker:
    #             width_tracker[height] = [skew, skew]
    #         else:
    #             # set left skew
    #             if skew < width_tracker[height][0]:
    #                 width_tracker[height][0] = skew
    #             # set right skew
    #             elif skew > width_tracker[height][1]:
    #                 width_tracker[height][1] = skew

    #         curr_skew = width_tracker[height][1] - width_tracker[height][0]
    #         if curr_skew > max_skew:
    #             max_skew = curr_skew

    #         widthDFSHelper(root.left, height + 1, skew - 1)
    #         widthDFSHelper(root.right, height + 1, skew + 1)

    #     widthDFSHelper(root, 0, 0)
    #     return max_skew
        


# 2^skew?
# heights: None, 0, 1, 2

def sampleTree1():
    """
           1
         /   \
        3     2
       / \     \  
      5   3     9 
    """
    n5 = TreeNode(None, None)
    n3b = TreeNode(None, None)
    n3a = TreeNode(n5, n3b)
    n9 = TreeNode(None, None)
    n2 = TreeNode(None, n9)
    n1 = TreeNode(n3a, n2)
    return n1, 4

def sampleTree2():
    """
          1
         /  
        3    
       / \       
      5   3
    """
    n5 = TreeNode(None, None)
    n3b = TreeNode(None, None)
    n3a = TreeNode(n5, n3b)
    n1 = TreeNode(n3a, None)
    return n1, 2

def sampleTree3():
    """
          1
         / \
        3   2 
       /        
      5
    """
    n5 = TreeNode(None, None)
    n3a = TreeNode(n5, None)
    n2 = TreeNode(None, None)
    n1 = TreeNode(n3a, n2)
    return n1, 2

def sampleTree4():
    """
          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
    """
    n6 = TreeNode(None, None)
    n5 = TreeNode(n6, None)
    n3a = TreeNode(n5, None)
    n7 = TreeNode(None, None)
    n9 = TreeNode(None, n7)
    n2 = TreeNode(None, n9)
    n1 = TreeNode(n3a, n2)
    return n1, 8

def sampleTree5():
    """
           1
         /   \
        3     2
       / \   /   
      5   3 8    
    """
    n5 = TreeNode(None, None)
    n3b = TreeNode(None, None)
    n3a = TreeNode(n5, n3b)
    n8 = TreeNode(None, None)
    n2 = TreeNode(n8, None)
    n1 = TreeNode(n3a, n2)
    return n1, 3

def sampleTree6():
    """
           1
         /    \
        3      2
       /\     /   
      5  3   8   x
     /        \
    7 x x x x 9 x  x
    """
    n7 = TreeNode(None, None)
    n5 = TreeNode(n7, None)
    n3b = TreeNode(None, None)
    n3a = TreeNode(n5, n3b)
    n9 = TreeNode(None, None)
    n8 = TreeNode(None, n9)
    n2 = TreeNode(n8, None)
    n1 = TreeNode(n3a, n2)
    return n1, 6

if __name__ == "__main__":
    print("=== widthOfBinaryTree ===")

    s = Solution()

    t1 = sampleTree1()
    assert s.widthOfBinaryTree(t1[0]) == t1[1]

    t2 = sampleTree2()
    assert s.widthOfBinaryTree(t2[0]) == t2[1]

    t3 = sampleTree3()
    assert s.widthOfBinaryTree(t3[0]) == t3[1]

    t4 = sampleTree4()
    assert s.widthOfBinaryTree(t4[0]) == t4[1]

    t5 = sampleTree5()
    assert s.widthOfBinaryTree(t5[0]) == t5[1]

    print("=== done! ===")

