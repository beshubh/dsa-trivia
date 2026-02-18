class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = set()

        def dfs(i = 0, cur_sum = 0, cur=[]):
            if cur_sum > target:
                cur.pop()
                return
            if cur_sum == target:
                res.add(tuple(sorted(cur)))
                return

            if i >= len(candidates):
                if cur_sum == target:
                    res.add(sorted(tuple(cur)))
                return
            # include
            dfs(i + 1, cur_sum + candidates[i], cur + [candidates[i]])
            # exclude
            dfs(i + 1, cur_sum, cur)
        dfs()
        return [list(x) for x in res]
