class Solution:
    def trap(self, height: List[int]) -> int:
        lenght=len(height)

        prefix= [0]*lenght
        prefix[0]= height[0]
        for i in range(1,lenght):
            if height[i]>prefix[i-1]:
                prefix[i]=height[i]
            else:
                prefix[i]=prefix[i-1]
        suffix= [0]*lenght
        suffix[-1]= height[-1]
        for i in range(lenght-2, -1,-1):
            if height[i]>suffix[i+1]:
                suffix[i]=height[i]
            else:
                suffix[i]=suffix[i+1]
        out=0
        for i in range(1,lenght-1):
            out+=min(max(prefix[i]-height[i],0),max(suffix[i]-height[i],0))
        return out

        

            


        