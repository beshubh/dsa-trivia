class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        target_array = -1
        left, right = 0, len(matrix) - 1
        #
        # matrix =
        # [
        #    [1,3,5,7],
        #    [10,11,16,20],
        #    [23,30,34,60]
        # ]
        # target=3
        #
        while left <= right: # 0, 0
            mid = right + left // 2 # 0
            row = matrix[mid] # [1,3,5,7]
            if target >= row[0] and target <= row[-1]: # 3 >= 1, 3 <= 7 true
                target_array = mid # 0
                break
            elif target > row[-1]: # 3 > 20, false
                left = mid + 1
            else:
                right = mid - 1 # 0

        print(target_array)
        if target_array == -1:
            return False
        if self.bin_search(matrix[target_array], target) == -1:
            return False
        return True

    def bin_search(self, array: list[int], target: int) -> int:
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            mid_val = array[mid]
            if target > mid_val:
                left = mid + 1
            elif target < mid_val:
                right = mid - 1
            else:
                return mid
        return -1
