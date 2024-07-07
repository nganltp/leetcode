def maxScore(s):
    """
    :type s: str
    :rtype: int
    """
    max_score = 0
    for i in range(1, len(s)):
        max_score = max(max_score, s[:i].count('0')+ s[i:].count('1'))
        # print(s[:i], s[i:])
    
    return max_score

s = '011101'
max_score = maxScore(s)
print(max_score)