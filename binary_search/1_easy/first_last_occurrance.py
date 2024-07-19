'''

Given a sorted integer array, find the index of a given number's first and last occurrence.

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 5
Output: (1, 3)
Explanation: The first and last occurrence of element 5 is located at index 1 and 3, respectively.

• If the target is not present in the array, the solution should return the pair (-1, -1).

Input: nums[] = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9], target = 4
Output: (-1, -1)

'''


def binary_search(nums, target, is_searching_left):
    low, high = 0, len(nums) - 1
    idx = -1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            idx = mid  # upadate idx
            if is_searching_left:
                high = mid - 1  # move to left
            else:
                low = mid + 1  # move to right    
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return idx


def findPair(nums: list[int], target: int) -> tuple[int]:
    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)
    return (left, right)


if __name__ == '__main__':
    # Case 1
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 5
    res = findPair(nums, target)
    expected = (1, 3)
    assert res == expected, f"{res} != {expected}"
    print('PASS')
    
    # Case 2
    nums = [5,7,7,8,8,10]
    target = 8
    res = findPair(nums, target)
    expected = (3, 4)
    assert res == expected, f"{res} != {expected}"
    print('PASS')
    
    # Case 3
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
    target = 4
    res = findPair(nums, target)
    expected = (-1, -1)
    assert res == expected, f"{res} != {expected}"
    print('PASS')

print(binary_search([1,2,3,3,3,4,5], 3, False))