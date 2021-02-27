class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)==0:
            l = len(nums2)
            return (nums2[int(l/2)]+nums2[int(l/2-0.5)])/2

        if len(nums2)==0:
            l = len(nums1)
            return (nums1[int(l/2)]+nums1[int(l/2-0.5)])/2

        # 让第一个序列更长
        if len(nums1)<len(nums2):
            return self.findMedianSortedArrays( nums2,nums1)
        
        # p1,p2 长度分别为m,n; 满足m>=n
        m = len(nums1)
        n = len(nums2)
        l = m+n
        # 定义l的一半为d
        d = (l+1)//2  

        # p1 被划分为长度为m1,m2两部分，left1 为较小子集的最大值，right1为较大子集的最小值
        m1_max = d
        m1_min = (m-n)//2

        m1 = m1_max
        m2 = m-m1       
        left1 = nums1[m1-1]
        if m2 == 0:
            right1 = 1e6+1
        else:
            right1 = nums1[-m2]

         # p2 被划分为长度为n1,n2两部分，left2 为较小子集的最大值，right2为较大子集的最小值
        n1 = d-m1
        n2 = n-n1   

        if n2==0:
            right2=1e6+1
        else:
            right2 = nums2[-n2]

        if n1==0:
            left2 = -1e6-1
        else:
            left2 = nums2[n1-1]

        while(left1>right2 or left2>right1):
            temp_m1 = (m1_max+m1_min)//2
            temp_m2 = m-temp_m1
            temp_n1 = d-temp_m1 
            temp_n2 = n-temp_n1  
            
            if temp_m1 == 0:
                left1 = -1e6-1
            else:
                left1 = nums1[temp_m1-1]

            if temp_m2 == 0:
                right1 = 1e6+1
            else:
                right1 = nums1[-temp_m2]

            if temp_n2==0:
                right2 = 1e6+1
            else:
                right2 = nums2[-temp_n2]

            if temp_n1==0:
                left2 = -1e6-1
            else:
                left2 = nums2[temp_n1-1]

            if left1>right2:
                m1_max = temp_m1
            elif left2>right1:
                m1_min = temp_m1

        if l%2 == 1:
            return max(left1,left2)
        else:
            return (max(left1,left2)+min(right1,right2))/2
