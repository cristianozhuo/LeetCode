class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 数列长度为n
        n = len(s)
        if n == 0: return 0
        # 从第一个字符开始统计，每次增加一个字符，得到的字符串记为dic，最长的字符串长度记为l
        dic = []
        l = 0
        initial = 0
      
        for i in range(n):
            dic.append(s[i])
            # dic新增加的字符为s[i]，若此时字符串dic中出现两次s[i]，则dic舍弃第一次s[i]及其之前的部分
            index = dic.index(s[i]) 
            if index+initial<i: 
                dic = dic[index+1:]
                initial = initial+index+1
            # 统计dic的长度，更新l 
            temp = len(dic)
            if temp> l : l = temp    
        return l
