# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)   # create dummy node
        dummy.next = head     # link dummy to head
        curr = dummy          # start from dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # skip node
            else:
                curr = curr.next            # move forward

        return dummy.next
