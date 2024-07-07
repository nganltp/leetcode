from collections import deque
def longestSubarray(nums, limit):
    """
    :type nums: List[int]
    :type limit: int
    :rtype: int
    """
    maxDeque, minDeque = deque(), deque()
    l = 0
    for r, num in enumerate(nums):
        while maxDeque and num > nums[maxDeque[-1]]:
            maxDeque.pop()
        while minDeque and num < nums[minDeque[-1]]:
            minDeque.pop()
        maxDeque.append(r)
        minDeque.append(r)
        if nums[maxDeque[0]] - nums[minDeque[0]] > limit:
            if maxDeque[0] == l:
                maxDeque.popleft()
            if minDeque[0] == l:
                minDeque.popleft()
            l += 1
    return r - l + 1

print(longestSubarray([8,2,4,7], 4)) #2
# print(longestSubarray([8,2,4,7], 4))