def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # backtracking
    # global stack 

    output = []
    stack = []
    def backtracking(openP, closeP):
        if openP == closeP == n:
            output.append("".join(stack))
            return
        if openP < n:
            stack.append("(")
            backtracking(openP + 1, closeP)
            stack.pop()
        if closeP < openP:
            stack.append(")")
            backtracking(openP, closeP + 1)
            stack.pop()

    backtracking(0,0)
    return output
    

n = 3
# stack = ""
print(generateParenthesis(n))
