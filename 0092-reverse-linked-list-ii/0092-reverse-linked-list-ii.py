# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        # Step 1: Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 2: Move `prev` to one node before the 'left' position
        for _ in range(left - 1):
            prev = prev.next

        # Step 3: Start reversing the sublist
        curr = prev.next
        next_node = None

        # Reverse nodes between left and right
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        # Step 4: Return the new head
        return dummy.next
