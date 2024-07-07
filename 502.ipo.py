import heapq
def findMaximizedCapital(k, w, profits, capital):
    projects = sorted(zip(capital, profits))
    max_heap = []

    i = 0
    for _ in range(k):
        while i < len(projects) and projects[i][0] <= w:
            heapq.heappush(max_heap, -projects[i][1])
            i += 1

        if not max_heap:
            break

        w -= heapq.heappop(max_heap)

    return w



k = 4 
w = 0
profits = [1,2,3,2,1,6,3]
capital = [0,3,4,2,1,4,1]

print(findMaximizedCapital(k, w, profits, capital))