def maxProfitAssignment(difficulty, profit, worker):
    """
    :type difficulty: List[int]
    :type profit: List[int]
    :type worker: List[int]
    :rtype: int
    """
    jobs = sorted(zip(difficulty, profit))
    print(jobs)
    # sorted_difficulty = [job[0] for job in sorted_jobs]
    # sorted_profit = [job[1] for job in sorted_jobs]
    worker.sort()
    max_num = jobs[0][1]
    profit = 0
    i = 0
    for w in worker:
        while i < len(jobs) and w >= jobs[i][0]:
            max_num = max(max_num, jobs[i][1])
            i += 1
        profit += max_num
    return profit

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
print(maxProfitAssignment(difficulty, profit, worker))  # Output: 100


