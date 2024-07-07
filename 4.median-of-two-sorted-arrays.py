def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if (len(nums1) + len(nums2))%2 == 0:
        is_even = True
    else:
        is_even = False
    
    k = (len(nums1) + len(nums2))//2

    check = 0
    i_nums1 = 0
    i_nums2 = 0
    while(check < k):

        if i_nums1 == len(nums1):
            k = k - len(nums1)
            if is_even:
                return (nums2[k] + nums2[k+1])/2
            else:
                return nums2[k]
        if i_nums2 == len(nums2):
            k = k - len(nums2)
            if is_even:
                return (nums1[k] + nums1[k+1])/2
            else:
                return nums1[k]

        if nums1[i_nums1] < nums2[i_nums2]:
            value = nums1[i_nums1]
            i_nums1 += 1
        else:
            value = nums2[i_nums2]
            i_nums2 +=1
            
        check += 1
        print(i_nums1, i_nums2, check, k)
    
    min_num = 0
    if len(nums1) == i_nums1:
        min_num = nums2[i_nums2]
    elif len(nums2) == i_nums2:
        min_num = nums1[i_nums1]
    else:
        min_num = min(nums1[i_nums1], nums2[i_nums2])
    if is_even:
        return (value + min_num)/2
    return min_num


nums1 = [1,2]
nums2 = [3,4]
output = findMedianSortedArrays(nums1, nums2)
print(output)
