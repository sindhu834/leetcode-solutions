class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> list[Optional[ListNode]]:
        # Step 1: Count total length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # Step 2: Determine base size and extra nodes
        base_size, extra = divmod(n, k)
        
        # Step 3: Split into k parts
        res = []
        curr = head
        
        for i in range(k):
            part_head = curr
            part_size = base_size + (1 if i < extra else 0)
            
            # Move (part_size - 1) steps ahead
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next
            
            # Cut the list here
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part
            
            res.append(part_head)
        
        return res
