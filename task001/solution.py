class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # 第i个数是 a=nums[i]，判断target-a 是否在 nums[i+1:] 中
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]: 
                return i,i+1+nums[i+1:].index(target-nums[i])
