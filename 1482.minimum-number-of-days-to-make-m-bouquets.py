def check_adjacent_flowers(bloomDay, day, k, m):
    count_m = 0
    group = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= day:
            group += 1
        else:
            count_m += group // k
            group = 0
    count_m += group // k
    return count_m >= m

def minDays(bloomDay, m, k) -> int:
    if m*k > len(bloomDay):
        return -1
    left = min(bloomDay)
    right = max(bloomDay)
    while left < right:
        mid = (left + right) // 2
        if check_adjacent_flowers(bloomDay, mid, k, m):
            right = mid
        else:
            left = mid + 1
    return left


bloomDay = [72,90,79,41,29,57,68,79,80,44,44,12,50,12,7,39,43,93,32]
m = 9
k = 2
print(minDays(bloomDay, m, k))  # Output: 93