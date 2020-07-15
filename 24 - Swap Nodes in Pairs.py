
# intuition
# the next of the firstnode is the result of the swap of the third&fourth nodes
# the next of the secondNode is the first one

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        _next = head.next
        head.next = self.swapPairs(_next.next)
        _next.next = head
        return _next