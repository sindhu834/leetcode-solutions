# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        nums_set = set(nums)  # O(1) lookups
        count = 0
        current = head
        
        while current:
            # If current node is in nums_set and next node is None or not in nums_set
            if current.val in nums_set and (not current.next or current.next.val not in nums_set):
                count += 1
            current = current.next  # move to next node
        
        return count
