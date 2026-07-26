class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        l=0
        r=k-1
        maxes=[]
        max_, idx= self.getMaxAdnIdx(nums[l:r+1])
        maxes.append(max_)
        while r<len(nums)-1:
            r+=1
            
            if idx==l:
                max_, idx= self.getMaxAdnIdx(nums[l+1:r])
                idx+=l+1
            l+=1
            if nums[r]>max_:
                max_=nums[r]
            maxes.append(max_)
        return maxes
    def getMaxAdnIdx(self, nums:List[int])->tuple:
        max_=float('-inf')
        for i in range(len(nums)):
            if nums[i]>max_:
                max_= nums[i]
                idx=i
        return max_, idx

        