from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        l=0
        r=k-1
        maxes=[]
        stck=deque([])
        for i in range(r+1):
            while stck and nums[i]>stck[-1]:
                stck.pop()
            stck.append(nums[i])
        maxes.append(stck[0])
        while r<len(nums)-1:
            r+=1
            if stck[0]==nums[l]:
                stck.popleft()
            l+=1
            
            while stck and nums[r]>stck[-1]:
                stck.pop()
            stck.append(nums[r])
            
            maxes.append(stck[0])
        return maxes



