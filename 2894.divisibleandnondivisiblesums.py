class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1=0
        nums2=0
        for i in range(1,n+1):
            if i %m!=0:
                nums1+=i
            else:
                nums2+=i    
            diff=nums1-nums2
        return diff        
