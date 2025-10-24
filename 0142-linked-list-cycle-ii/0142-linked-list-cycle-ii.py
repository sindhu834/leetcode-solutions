class Solution:
    def detectCycle(self, head):
        slow = fast = head
        
        # Step 1: Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle found
                break
        else:
            return None  # no cycle
        
        # Step 2: Find the entry point of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # the start node of cycle
