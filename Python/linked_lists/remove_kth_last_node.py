from typing import List

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def remove_kth_element(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        slow = fast = dummy

        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
