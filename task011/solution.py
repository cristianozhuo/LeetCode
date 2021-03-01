class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        v = 0
        while(i<j):
            v = max(v,min(height[i],height[j])*(j-i))
            if height[i]<height[j]: i+=1
            else : j-= 1
        return v
