def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    indices = [i for i, num in enumerate(nums) if num % 2 == 1]
    indices = [-1] + indices + [len(nums)]
    output = 0

    for i in range(1, len(indices) - k):
        left = indices[i] - indices[i-1]
        right = indices[i+k] - indices[i+k-1]
        output += left * right

    return output

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays(nums, k))