def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    result = []
    for i in range(len(words[0])):
        if all(words[0][i] in word for word in words[1:]):
            result.append(words[0][i])
            words[1:] = [word.replace(words[0][i], '', 1) for word in words[1:]]
    return result

words = ["cool","lock","cook"]
# return: ["c","o"]
print('return: ', commonChars(words))