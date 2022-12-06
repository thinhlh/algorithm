class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        next = head.next
        if next != None:
            head.next = next.next
            next.next = head

            # Continuous ly assign next with recursion
            head.next = self.swapPairs(head.next)
            return next
        else:
            return head

        # while head != None:
        #     next = head.next

        #     if next == None:
        #         break
        #     head.next = next.next
        #     next.next = head
        #     next = next.next

        # return temp


print(Solution().swapPairs(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
