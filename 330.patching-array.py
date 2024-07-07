def minPatches(nums, n):
    patches = 0
    i = 0
    checked = 1
    while checked <= n:
        if i < len(nums) and nums[i] <= checked:
            checked += nums[i]
            i += 1
        else:
            checked *= 2
            patches += 1

    return patches

# Ví dụ sử dụng
print(minPatches([1], 10))  # Output: 1
print(minPatches([1, 5, 10], 20))  # Output: 2
print(minPatches([1, 2, 2], 5))  # Output: 0


'''
[1], [2, 3]=> 6
1,2,3,4 => 10

1: 1
2: 2
3: 1,2
4: 1,3
5: 
6: 1,5
7: 2,5 
'''
