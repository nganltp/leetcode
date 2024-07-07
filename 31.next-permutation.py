def nextPermutation(nums):
	"""
	:type nums: List[int]
	:rtype: None Do not return anything, modify nums in-place instead.
	"""
	for i in range(len(nums) - 1, -1, -1):
		print(i, nums[i])

nums = [1,2,3]                                                                                             
print(nextPermutation(nums))  
    