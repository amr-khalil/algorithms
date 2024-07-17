'''
Given a sorted integer array and a target, determine if the target exists in the array in logarithmic time. If target exists in the array, the procedure should return the index of it.

Input: nums[] = [2, 3, 5, 7, 9], target = 7
Output: 3
Explanation: Element found at 4th (index 3) position

• If there are duplicate elements in the array, the procedure may return any index whose element is equal to the target.

Input: nums[] = [1, 2, 3, 4, 4, 5, 6, 7], target = 4
Output: 3 (or 4)
Explanation: Element found at the 4th (index 3) or 5th (index 4) position.

• If the target is not located, the procedure should return -1.

Input: nums[] = [1, 4, 5, 8, 9], target = 2
Output: -1
'''

def findIndex(nums: list[int], target: int) -> int:
    l, r = 0, len(nums)-1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        
    return -1
        

if __name__ == '__main__':
    # Case 1
    nums = [2, 3, 5, 7, 9]
    target = 7
    assert findIndex(nums, target) == 3, f"{findIndex(nums, target)} != 3"
    print('PASS')
    
    # Case 2
    nums = [1, 2, 3, 4, 4, 5, 6, 7]
    target = 4
    assert findIndex(nums, target) == 3, f"{findIndex(nums, target)} != 4"
    print('PASS')
    
    # Case 3
    nums = [1, 4, 5, 8, 9]
    target = 2
    assert findIndex(nums, target) == -1, f"{findIndex(nums, target)} != -1"
    print('PASS')
    
    