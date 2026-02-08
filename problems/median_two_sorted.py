import unittest

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        X, Y = sorted([nums1, nums2], key=len)
        # X = [2] 
        # Y = [1, 3]
        # T = 3
        left, right = 0, len(X) # 0, 1
        half = (len(X) + len(Y) + 1) // 2 # 2
        while left <= right: # 0, 1
            part_x = (left + right) // 2
            part_y = half - part_x

            # if part_x is 0, there is nothing on left side.
            # if part_x is lenth of x, there is nothing on the right side.
            max_left_x = float('-inf') if part_x == 0 else X[part_x - 1]
            min_right_x = float('inf') if part_x == len(X) else X[part_x]


            max_left_y = float('-inf') if part_y == 0 else Y[part_y - 1]
            min_right_y = float('inf') if part_y == len(Y) else Y[part_y]
            

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # found the solution
                # TODO: add the final logic
                N = len(X) + len(Y)
                if N % 2 == 0:
                    return float((max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2)
                else:
                    return float(max(max_left_x, max_left_y))
                
            elif max_left_x > min_right_y:
                # we need to move towards left in smaller, because this max_smaller_left should be part of the right partition.
                right = part_x - 1
            else:
                left = part_x + 1 # 3 # TODO: EDGE CASE, it will prematurely break if one array contains all the elements larger than other.
        
        raise ValueError(f'No solution for {nums1} and {nums2}')

        

class TestMedianTwoSorted(unittest.TestCase):
    def setUp(self):
        self._runner = Solution()

    def test_even(self):
        X = [1, 2, 3]
        Y = [4, 5, 6]
        self.assertEqual(self._runner.findMedianSortedArrays(X, Y), 3.5)
    
    def test_odd(self):
        X = [1, 2, 3]
        Y = [4, 5]
        self.assertEqual(self._runner.findMedianSortedArrays(X, Y), 3)
    

    def test_different(self):
        X = [10, 12, 15, 16]
        Y = [ 1, 2, 3, 5, 6]
        self.assertEqual(self._runner.findMedianSortedArrays(X, Y), 6)
    
    def test_empty(self):
        X = []
        Y = [1, 2, 3, 4]
        self.assertEqual(self._runner.findMedianSortedArrays(X, Y), 2.5)
    
    def test_edge(self):
        X = [2]
        Y = [1, 3]
        self.assertEqual(self._runner.findMedianSortedArrays(X, Y), 2.0)


if __name__ == '__main__':
    unittest.main()
