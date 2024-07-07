def numberOfAlternatingGroups(colors):
    """
    :type colors: List[int]
    :rtype: int
    """
    if len(colors) == 3:
        if sum(colors) in [1, 2]:
            return 1
        else:
            return 0
    count = 0 #len = 4
    if colors[-1] != colors[-2] and colors[-1] != colors[0]:
        count+= 1
    if colors[-1] != colors[0] and colors[0] != colors[1]:
        count+=1
        # 0,1,0,0
            
    for i in range(len(colors)-2):
        print(i, colors[i], colors[i+1], colors[i+2])
        if colors[i] != colors[i+1] and colors[i+1] != colors[i+2]:
            count+=1
    return count

print(numberOfAlternatingGroups([0,1,0,0,1])) #1