# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head
        after = after_head
        current = head
        
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        # Merge lists
        before.next = after_head.next
        after.next = None
        
        return before_head.next
