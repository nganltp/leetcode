def largestGoodInteger(num):
    """
    :type num: str
    :rtype: str
    """
    intergers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
    for i in intergers:
        if i in num:
            return i
    return ""
num = "6777133339"
output = largestGoodInteger(num)
print(output)