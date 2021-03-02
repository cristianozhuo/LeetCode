class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        if n<= 2: return []

        s = []
        nums.sort()
        a = -10**5 -1

        for i in range(n-2):
            if nums[i]>0: return s
            if nums[i]>a:
                a = nums[i]
                j = i+1
                k = n-1
                while j<k:
                    b = nums[j]
                    c = nums[k]
                    if a+b+c<0:
                        j = j+1
                        while nums[j] == b:
                            if j==k: break
                            j = j+1
                            

                    elif a+b+c>0:
                        k = k-1
                        while nums[k] == c:
                            if k==j: break
                            k = k-1
                                            
                    else: 
                        s.append([a,b,c])
                        j = j+1
                        k = k-1
                        
                        while nums[j] == b:
                            j = j+1
                            if j>=k: break

                        while nums[k] == c:
                            k = k-1
                            if k<=j: break
        return s
