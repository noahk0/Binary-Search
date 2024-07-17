class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        val = self.map[key]

        if val and val[-1][0] <= timestamp:
            return val[-1][1]

        l, r = 0, len(val) - 1

        while l < r:
            if val[l][0] <= timestamp < val[l + 1][0]:
                return val[l][1]

            mid = (l + r) // 2
            
            if val[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return ''
