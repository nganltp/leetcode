def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    output = [""]*numRows
    index_output = 0
    forward = True
    for i in s:
        output[index_output] += i
        if index_output == numRows -1:
            forward = False
        elif index_output == 0:
            forward = True
        if forward:
            index_output += 1
        else:
            index_output -=1
    
    return "".join(output)
        

print(convert("ABC", 1))