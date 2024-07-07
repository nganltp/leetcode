import copy
def avg(i, j, img):
    count = 9
    sum = 0
    for m in range(i-1, i + 2):
        for n in range(j-1, j+2):
            if m < 0 or n < 0 or m > len(img) -1 or n > len(img[i]) -1:
                count -= 1
            else:
                sum += img[m][n]
    return int(sum/count)

def imageSmoother(img):
    """
    :type img: List[List[int]]
    :rtype: List[List[int]]
    """
    output = copy.deepcopy(img)
    for i in range(len(img)):
        for j in range(len(img[i])):
            print(img[i][j])
            output[i][j] = avg(i, j, img)
    
    return output

img = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
output = imageSmoother(img)
print(output) 