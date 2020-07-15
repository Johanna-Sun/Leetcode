

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        result = ListNode(0, head)
        dummy = ListNode(0, head)
        first = result.next
        second = first.next

        while first.next is not None:

            first.next = second.next
            second.next = first
            dummy.next = second

            if result.val == 0:
                result.next = second
                result.val = 1

            if first.next is None:
                break

            dummy = first
            print("dummy:", dummy.val)
            first = first.next
            print("first: ", first.val)
            second = first.next
            print("second: ", second.val)

        return result.next