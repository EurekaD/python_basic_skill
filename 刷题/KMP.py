"""
算法核心思想：尽可能利用残余的信息 【最大限度的利用已经花费的代价，充分利用已经得到的信息】

"""


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pi[i] = j

        print("pi:{}".format(pi))
        j = 0
        for i in range(n):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1


x = Solution.strStr("oashfkasfdivkhaskjfakhfcivdiv", "divdiv")
print(x)