class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=k
        while r<len(arr):
            if abs(arr[r]-x) < abs(arr[l]-x):
                l+=1
                r+=1
            elif abs(arr[r]-x) == abs(arr[l]-x) and arr[r]<=arr[l] :
                l+=1
                r+=1
            else:
                break
        return arr[l:r]
            
        

        