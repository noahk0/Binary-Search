def search(self, nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        idx = (l + r) // 2
        
        if target < nums[idx]:
            r = idx - 1
        elif nums[idx] < target:
            l = idx + 1
        else:
            return idx

    return -1
