# Solved
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def preOrder(root: Node):
    # Write your code here
    if root:
        print(root.info, end=' ')
        preOrder(root.left)
        preOrder(root.right)


def postOrder(root: Node):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.info, end=' ')


def inOrder(root: Node):
    if root:
        inOrder(root.left)
        print(root.info, end=' ')
        inOrder(root.right)


def getHeight(root: Node):
    if not root:
        return 0
    else:
        max_left, max_right = 0, 0 
        max_left += 0 if not root.left else 1 + getHeight(root.left) # Only start adding if have left node
        max_right += 0 if not root.right else 1 + getHeight(root.right) # Only start adding if have right node
        return max(max_left, max_right)


tree = BinarySearchTree()

for a in [4, 2, 6, 1, 3, 5, 7]:
    tree.create(a)
print(getHeight(tree.root))

# tree = BinarySearchTree()
# for a in [1, 2, 5, 3, 4, 6]:
#     tree.create(a)
