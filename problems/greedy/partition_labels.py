class Solution:
    def partitionLabels(self, s: str) -> list[int]:  # x, y, x, z, b, z, a
        last_occ = {}
        for i, c in enumerate(s):
            last_occ[c] = i
        result = []  # [3, ]
        # { x: 2, y: 1, z: 5, b: 4, a: 6}
        size, end = 0, 0  # 3, 0
        for i, c in enumerate(s):  # 5, b
            size += 1
            end = max(last_occ[c], end)  # (4, 5) -> 5
            if i == end:  # 4 == 5, false
                result.append(size)
                size = 0
        return result
