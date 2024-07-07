def minKBitFlips(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n = len(nums)
    res = 0
    check = 0
    flip_index = 0
    for i in range(n - k + 1):
        if i >= flip_index:
            check = 0
        else:
            check = 1
        if nums[i] == check:
            flip_index = i + k
            # Flip the bits in the segment nums[i:i+k]
            # for j in range(i, i + k):
            #     nums[j] ^= 1
            res += 1
    if any(num == 1 - check for num in nums[i+1:flip_index]):
        return -1
    if any(num == 0 for num in nums[flip_index:]):
        return -1
    return res

# print(minKBitFlips([0,1,0], 1)) #2
print(minKBitFlips([0,0,0,1,0,1,1,0], 3)) #3
# print(minKBitFlips([0,1], 2)) #-1
# nums = 
# print(minKBitFlips(nums, 15295)) #-1


# Time complexity: O(n)


    