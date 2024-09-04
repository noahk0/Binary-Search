def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    if nums[0] <= nums[-1]:
        return nums[0]

    while l < r:
        idx = (l + r) // 2

        if nums[idx + 1] < nums[idx]:
            return nums[idx + 1]

        if nums[l] < nums[idx]:
            l = idx + 1
        else:
            r = idx
