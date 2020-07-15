# intuition
# first thought: change the data structure to be a circle / double link
# then: if we cant count from the back, then we just save one at the beginning

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:


        dummy = ListNode(0,head)

        first = dummy
        second = head
        i = 0

        while i < n:
            second = second.next
            i += 1

        while second is not None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next

