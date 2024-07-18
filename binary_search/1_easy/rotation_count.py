'''

Given a circularly sorted array of distinct integers, find the total number of times the array is rotated. You may assume that the rotation is in anti-clockwise direction.

Input: [8, 9, 10, 2, 5, 6]
Output: 3

Input: [2, 5, 6, 8, 9, 10]
Output: 0

'''

def findRotationCount(nums: list[int]) -> int:
    """Hint: return the index of the lowest element"""
    low, high = 0, len(nums) - 1
    
    while low <= high:
        # if the array is already sorted, return low (0 rotation)
        if nums[low] <= nums[high]:
            return low
        
        mid = (low + high) // 2
        # find the next and previous element of the `mid` element (in circular manner)
        next_mid = (mid + 1) % len(nums)
        prev_mid = (mid - 1 + len(nums)) % len(nums)
        
        # if the `mid` element is less than both its next and previous
        # neighbor, it is the list's minimum element (10, 2, 3)
        if nums[mid] <= nums[next_mid] and nums[mid] <= nums[prev_mid]:
            return mid
        
        # Decide if to search in the left half or the right half
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1
    
    
if __name__ == '__main__':
    # Case 1
    nums = [8, 9, 10, 2, 5, 6]
    assert findRotationCount(nums) == 3, f"{findRotationCount(nums)} != 3"
    print('PASS')
    # Case 2
    nums = [2, 5, 6, 8, 9, 10]
    assert findRotationCount(nums) == 0, f"{findRotationCount(nums)} != 0"
    print('PASS')
