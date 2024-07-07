def threeSum(nums):
    output = []
    output_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) -1):
            # print(i, j, nums[:i] + nums[i+1:j] + nums[j+1:])
            if -(nums[i] + nums[j]) in nums[:i] + nums[i+1:j] + nums[j+1:]:
                triplets= [nums[i], nums[j], -(nums[i] + nums[j])]
                triplets = sorted(triplets)
                if triplets not in output:
                    output.append(triplets)

                    
    return output
nums = [-1,0,1,2,-1,-4]
output = threeSum(nums)
print(output)