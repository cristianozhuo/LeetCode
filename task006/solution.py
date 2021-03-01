class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        r = 2*numRows-2
        s_set = ["" for i in range(numRows)]

        for i in range(len(s)):
            d = i%r
            d = min(d,r-d)
            s_set[d] += s[i]
        
        re_s = ""
        for i in range(numRows):
            re_s += s_set[i]
        return re_s
