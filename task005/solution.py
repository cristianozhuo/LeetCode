class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {}
        n = len(s)
        for i in range(n):
            if s[i] not in dic.keys():
                dic[s[i]] = [i]
            else:
                dic[s[i]].append(i)      
        l = 0
        re_s = s[0]
        for k in dic.keys():
            temp_n = len(dic[k])
            if temp_n>1:
                for j in range(1,temp_n)[::-1]:
                    for m in range(j):
                        if dic[k][j]+1 - dic[k][m] > l:
                            temp_s = s[dic[k][m]:dic[k][j]]+s[dic[k][j]]
                            if temp_s == temp_s[::-1]:
                                re_s = temp_s
                                l = dic[k][j]+1 - dic[k][m]
                                break
        return re_s
