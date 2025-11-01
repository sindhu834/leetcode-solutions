class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr:
            if curr.val in remove_set:
                prev.next = curr.next  # skip this node
            else:
                prev = curr
            curr = curr.next

        return dummy.next
