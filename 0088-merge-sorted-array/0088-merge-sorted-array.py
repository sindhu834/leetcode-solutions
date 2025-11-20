class Solution:
    def merge(self, nums1, m, nums2, n):

        # 1️⃣ Pointers to the last used elements
        i = m - 1     # last element in nums1 that contains real data
        j = n - 1     # last element in nums2
        k = m + n - 1 # last index of nums1 (full size)

        # 2️⃣ Compare from the END of both arrays
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # 3️⃣ If nums2 has leftovers, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
