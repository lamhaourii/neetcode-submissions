class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        most=0
        while l<r:
            current= (r-l)*min(heights[r],heights[l])
            if current>most:
                most=current
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return most


        