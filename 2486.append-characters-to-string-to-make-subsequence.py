def appendCharacters(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_index = 0
        for i in range(len(t)):
            print(i, t[i])
            for j in range(s_index, len(s)):
                s_index = j + 1
                if t[i] == s[j]:

                    break
            if s_index == len(s) and t[i] == s[j]:
                return len(t) - i - 1
            elif s_index == len(s) and t[i] != s[j]:
                return len(t) - i
        return 0

s = "lxvqffcj"
t = "vjtgatotj"
print('return: ', appendCharacters(s, t))