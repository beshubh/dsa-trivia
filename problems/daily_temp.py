

class Solution:
    def dailyTemperatures(self, temperatures: list[int]):
        indices = []
        result = [0] * len(temperatures)
        for i in reversed(range(len(temperatures))):
            if i == len(temperatures) - 1:
                continue
            while indices and temperatures[indices[-1]] < temperatures[i]:
                indices.pop()

            if indices:
                result[i] = indices[-1] - i
            indices.append(i)
        return indices
