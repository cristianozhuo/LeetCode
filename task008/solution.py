class Solution:
    def myAtoi(self, s: str) -> int:  
           
        sign = 1
        re_s = "0"      
        num_set = ["0","1","2","3","4","5","6","7","8","9"]

        s = s.lstrip()+"a"

        if s[0]=="+": 
            pass
        elif s[0]=="-": 
            sign = -1
        elif s[0]  in num_set:
            re_s = re_s+s[0]
        else:
            return 0
        
        for i in range(1,len(s)):
            if s[i] in num_set:
                re_s = re_s+s[i]
            else:
                break

        return max(min(int(re_s)*sign,2**31-1),-2**31)
