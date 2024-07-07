def min_pair(num, min_1, min_2): #min_1 < min_2
    if num < min_1: #num < min_1 < min_2
        return num, min_1
    elif num < min_2: #min_1 < num < min_2
        return min_1, num
    else:
        return min_1, min_2

def max_pair(num, max_1, max_2): #max_1 < max_2
    if num > max_2: #max_1 < max_2 < num
        return max_2, num
    elif num > max_1: #max_1 < num < max_2
        return num, max_2
    else:
        return max_1, max_2

def maxProductDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_1 = max_1 = min(nums[0], nums[1])
    min_2 = max_2 = max(nums[0], nums[1])
    for i in nums[2:]:
        min_1, min_2 = min_pair(i, min_1, min_2)
        max_1, max_2 = max_pair(i, max_1, max_2)
    return (max_1 * max_2) - min_1 * min_2
nums = [1,6,7,5,2,4,10,6,4]
output = maxProductDifference(nums)
print(output)