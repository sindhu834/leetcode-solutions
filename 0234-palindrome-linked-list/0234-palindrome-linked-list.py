# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current = head
        
        # Step 1: Store all node values in a list
        while current:
            vals.append(current.val)
            current = current.next
        
        # Step 2: Check if the list is equal to its reverse
        return vals == vals[::-1]
