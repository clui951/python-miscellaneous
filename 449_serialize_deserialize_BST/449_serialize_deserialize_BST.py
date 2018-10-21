# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Pre-order traversal of tree
    # root of tree is first element of list
    # then all of left subtree, and all of right subtree
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def pre_order(node):
            if node == None:
                return []

            tree_list = []
            tree_list.append(str(node.val))

            left_list = pre_order(node.left)
            if left_list != []:
                tree_list.extend(left_list)
            right_list = pre_order(node.right)
            if right_list != []:
                tree_list.extend(right_list)

            return tree_list

        pre_order_list = pre_order(root)
        pre_order_string = ",".join(pre_order_list)
        return pre_order_string
        

    # Building BST from a pre-order traversal list
    # Use nested function to process each value once
    # Use range to determine left and right subtrees
    # Popped element is the root
    #   left subtree should be all values from current min, to the root value
    #   right subtree should be all values from root value to current max

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        pre-order traversal to tree structure
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        vals = [int(x) for x in data.split(",")]
        def build_from_pre_order(min_val, max_val):
            if len(vals) > 0 and min_val < vals[0] < max_val:
                val = vals.pop(0)
                node = TreeNode(val)
                node.left = build_from_pre_order(min_val, val)
                node.right = build_from_pre_order(val, max_val)
                return node

        return build_from_pre_order(-float("inf"), float("inf"))
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    print("=== Serialize deserialize BST ===")

    c = Codec()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(6)
    print(c.serialize(root))
    print(c.deserialize(c.serialize(root)))

    print("one serialize")
    print(c.serialize(root))
    print("one serialize, deserialize, serialize")
    print(c.serialize(c.deserialize(c.serialize(root))))

    print('\n\n----')
    des_tree = "41,37,24,1,0,2,4,3,9,7,6,5,8,11,10,16,15,12,13,14,19,18,17,20,22,21,23,35,30,29,26,25,27,28,32,31,34,33,36,39,38,40,44,42,43,48,46,45,47,49"
    print(des_tree)
    print(c.serialize(c.deserialize(des_tree)))


    print("=== done! ===")