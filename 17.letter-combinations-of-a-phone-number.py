mapping = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z']
    }
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    output = mapping[digits[0]]
    len_output = len(output)
    for i in digits[1:]:
        temp = output[:]
        output = []

        sub_digit = mapping[i]

        for m in temp:
            for n in sub_digit:
                output.append(m+n)
                print(output)
        


        
    return output

digits = "23"
print(letterCombinations(digits))