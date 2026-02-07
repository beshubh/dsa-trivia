class Solution:

    def bin_search(self, a: list[int], l: int, r: int, target: int):
        while l <= r: # 4 <= 4
            mid = (l + r) // 2 # 4
            if a[mid] == target: # 0 == 0
                return mid
            if target < a[mid]: # 0 < 1 yes
                r = mid - 1 # 4
            else:
                l = mid + 1
        return -1

    def search(self, nums: list[int], target: int) -> int:
        # 3 4 5 6 0 1 2, target = 2
        # 0 1 2 3 4 5 6
        left, right = 0, len(nums) - 1
        while left <= right: # 4, 6
            print('left: ', left, 'right: ', right)
            if nums[left] < nums[right]: # array is sorted
                return self.bin_search(nums, left, right, target)
            mid = (left + right) // 2 # 3
            pivot = nums[mid] # 6
            if pivot == target:
                return mid
            if pivot > nums[right]: # 6 > 2, yes
                # we are currently in the left sub array
                if target > pivot: # it should be in left sub array | 0 > 6 no
                    right = mid - 1
                else: # it should be the right sub array
                    left = mid + 1
            else: # pivot < nums[right]
                if target > pivot: # 2 > 1 yes
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
