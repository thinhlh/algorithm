# NOT YET SOLVED
class TreeNode:
    def __init__(self, value: int, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def add_node(self, value):
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.add_node(self.left)
        else:
            if not self.left:
                self.right = TreeNode(value)
            else:
                self.add_node(self.right)


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        pass

    def arr_to_tree_node(self, arr) -> TreeNode:

        root = TreeNode(arr[0])
        for i in range(1, len(arr)):
            if not arr[i]:
                continue
            root.add_node(arr[i])
        pass


Solution().arr_to_tree_node(
    [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
