class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l=len(heights)
        if len(heights)==1:
            return heights[0]
        
        left_smaller=[-1]*l
        right_smaller=[-1]*l
        stack=[]
        for i in range(l):
            while stack and heights[i]<stack[-1][0]:
                right_smaller[stack[-1][1]]=i
                stack.pop()
            stack.append((heights[i],i))

        stack=[]
        for i in range(l-1,-1,-1):
            while stack and heights[i]<stack[-1][0]:
                left_smaller[stack[-1][1]]=i
                stack.pop()
            stack.append((heights[i],i))

        largest=0
        for i in range(l):
            if right_smaller[i]==-1:
                right_smaller[i]=l
            
            current= heights[i]* (right_smaller[i]-left_smaller[i]-1)
            if current>largest:
                largest=current
            
        return largest
        
        

        



            
