def minEatingSpeed(self, piles: List[int], h: int) -> int:
    low = 1
    speed = high = max(piles)

    while low <= high:
        time, mid = 0, (low + high) // 2

        for pile in piles:
            time += ceil(pile / mid)

        if h < time:
            low = mid + 1
        else:
            high = mid - 1
            speed = mid

    return speed
