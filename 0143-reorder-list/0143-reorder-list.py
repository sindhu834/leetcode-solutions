class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow.next
        slow.next = None  # break the list into two halves
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
