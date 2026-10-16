class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        if m + n == 0:
            raise ValueError("At least one array must be non-empty")
        low, high, half = 0, m, (m + n + 1) // 2
        while low <= high:
            i = (low + high) // 2
            j = half - i
            l1 = float("-inf") if i == 0 else nums1[i - 1]
            r1 = float("inf") if i == m else nums1[i]
            l2 = float("-inf") if j == 0 else nums2[j - 1]
            r2 = float("inf") if j == n else nums2[j]
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            if l1 > r2: high = i - 1
            else: low = i + 1
        raise ValueError("Input arrays must be sorted")
