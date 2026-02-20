class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # sort the array so same elements are adjacent
        # which will allows us to skip the elements that are the same as the one we choose to include into our result set
        candidates = sorted(candidates)

        def dfs(i = 0, cur_sum = 0, cur=[]):
            if cur_sum > target:
                cur.pop()
                return
            if cur_sum == target:
                res.append(cur)
                return

            if i >= len(candidates):
                if cur_sum == target:
                    res.append(cur)
                return
            # include
            dfs(i + 1, cur_sum + candidates[i], cur + [candidates[i]])
            # skip all the elements that are similar to the one we chose to include
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # exclude
            dfs(i + 1, cur_sum, cur)

        dfs()
        return [list(x) for x in res]
