def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    start, end, leng = 0, len(nums1) - 1, (len(nums1) + len(nums2)) // 2

    while True:
        mid1 = (start + end) // 2
        mid2 = leng - mid1 - 2

        pre1, pre2, nxt1, nxt2 = nums1[mid1] if 0 <= mid1 else float('-inf'), nums2[mid2] if 0 <= mid2 else float('-inf'), nums1[mid1 + 1] if mid1 + 1 < len(nums1) else float('inf'), nums2[mid2 + 1] if mid2 + 1 < len(nums2) else float('inf')

        if pre1 <= nxt2 and pre2 <= nxt1:
            return min(nxt1, nxt2) if (len(nums1) + len(nums2)) % 2 else (max(pre1, pre2) + min(nxt1, nxt2)) / 2
        elif nxt2 < pre1:
            end = mid1 - 1
        else:
            start = mid1 + 1
