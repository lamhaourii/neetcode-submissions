class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1:
            return 1 if nums[0]==target else 0
        l=0
        r=1
        sum_=nums[0]+nums[1]
        min_= float('inf')
        while l<r and r<len(nums):
            if nums[r]>= target or nums[l]>=target:
                return 1
            if sum_>=target:
                sum_-=nums[l]
                if r-l+1 < min_:
                    min_=r-l+1
                l+=1
                
            if sum_<target:
                r+=1
                if r<len(nums):
                    sum_+=nums[r]
            
        return 0 if  min_== float('inf') else min_


                
            