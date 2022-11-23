# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    [5, 4, 3, 2, 1]

    def reverse_linked_list(self, head: ListNode) -> ListNode:
        # res = ListNode(head.val)
        res: ListNode = None
        while head != None:
            res = ListNode(head.val, res)
            head = head.next

        return res

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_linked_list = self.reverse_linked_list(head)

        prev = reversed_linked_list
        cur = reversed_linked_list
        for i in range(n):
            prev = cur
            cur = cur.next


print(
    Solution().removeNthFromEnd(head=ListNode(
        1,
        ListNode(2,
                 ListNode(3,
                          ListNode(4,
                                   ListNode(5)
                                   )
                          )
                 )
    ), n=2).val)
