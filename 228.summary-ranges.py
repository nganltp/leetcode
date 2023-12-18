def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output = []
        start_num = nums[0]
        end_num = nums[0]
        for n in nums[1:]:
            if n - end_num == 1:
                end_num = n
            else:
                if start_num == end_num:
                    output.append(str(start_num))
                else:
                    output.append(str(start_num) + '->' +str(end_num))
                
                start_num = end_num = n
        
        if start_num == end_num:
            output.append(str(start_num))
        else:
            output.append(str(start_num) + '->' +str(end_num))

        return output

nums = [0,1,2,4,5,7]
print(summaryRanges(nums))