class Solution:
    def trap(self, height: List[int]) -> int:
        v = 0
        while len(height) > 2:
            if height[0]==0:
                height = height[1:]
                continue
            if height[-1] ==0 : 
                height = height[:-1]
                continue
            break
        n = len(height)
        i = 0 
        j = n-1
        while(i+1<j):
            if height[i]<height[j]:
                v += max(0,height[i]-height[i+1])
                height[i+1] = max(height[i],height[i+1])
                i = i+1
            else:
                v += max(0,height[j]-height[j-1])
                height[j-1] = max(height[j],height[j-1])
                j = j-1
        return v
