def maxWidthOfVerticalArea(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    horizon = []
    for i in points:
        horizon.append(i[0])
    horizon = sorted(horizon)
    widest = 0
    for i in range(1, len(horizon)-1):
        widest = max(widest, horizon[i] - horizon[i-1])
    return widest

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
output = maxWidthOfVerticalArea(points)
print(output)