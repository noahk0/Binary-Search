def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    l, div = 0, len(matrix[0])
    r = div * len(matrix) - 1

    while l <= r:
        idx = (l + r) // 2
        mid = matrix[idx // div][idx % div]

        if mid < target:
            l = idx + 1
        elif target < mid:
            r = idx - 1
        else:
            return True
        
    return False
