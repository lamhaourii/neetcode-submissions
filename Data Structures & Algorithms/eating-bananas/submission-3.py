import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_ = max(piles)
        k=max_
        l=1
        r=max_ 
        while l<=r:
            mid=(l+r)//2
            long= self.getHours(piles, mid)
            if long<=h:
                r=mid-1
                k=mid
            else:
                l=mid+1
        return k





    def getHours(self, piles:List[int], k:int):
        hours=0
        for banana in piles:
            hours+=math.ceil(banana/k)
        return hours

