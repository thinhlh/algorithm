class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_l1 = 0
        l1_idx = 0
        sum_l2 = 0
        l2_idx = 0
        while l1 != None:
            sum_l1 += l1.val * 10**l1_idx
            l1_idx += 1
            l1 = l1.next
        while l2 != None:
            sum_l2 += l2.val * 10**l2_idx
            l2_idx += 1
            l2 = l2.next

        sum_l1_l2 = sum_l1+sum_l2

        res = ListNode()
        iteration = res

        while sum_l1_l2 > 0:
            iteration.val = sum_l1_l2 % 10
            sum_l1_l2 //= 10
            if (sum_l1_l2 > 0):
                iteration.next = ListNode()
                iteration = iteration.next
        return res


nodes = Solution().addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4)))
)
