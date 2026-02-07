


def bin_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        cur = arr[mid]
        if target < cur:
            right = mid - 1
        elif target > cur:
            left = mid + 1
        else:
            return mid
    return -1
