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
            speed, high = mid, mid - 1

    return speed
