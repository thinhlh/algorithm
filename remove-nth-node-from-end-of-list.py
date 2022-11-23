# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:

    def reverse_linked_list(self, head: ListNode) -> ListNode:
        res: ListNode = None
        while head != None:
            res = ListNode(head.val, res)
            head = head.next

        return res

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_linked_list = self.reverse_linked_list(head)

        cursor: ListNode = None
        i = 0
        while reversed_linked_list != None:
            if (i+1 == n):
                if(reversed_linked_list.next != None):
                    reversed_linked_list = reversed_linked_list.next
                else:
                    # The node need to be removed is the last node
                    # cursor.next = None
                    break

            cursor = ListNode(reversed_linked_list.val, cursor)
            reversed_linked_list = reversed_linked_list.next

            i += 1

        return cursor


# This is the optimized solution.
# First we will instantiation 2 pointer fast & slow.
# The **fast** pointer will traverse and go ahead the **slow** one n nodes.
# So basically whenever the fast.next is None (fast is the last node), the next slow.next is the pointer at n from end
# We just need to remove the slow.next
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        # Go ahead slow n times
        for _ in range(n):
            fast = fast.next
        if fast == None:
            return head.next
        else:
            # Continue to traverse, it fast.next is None then the next of slow is the node need to be removed
            while fast.next:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next

        return head


print(Solution2().removeNthFromEnd(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))
