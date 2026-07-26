class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        
        while l<=r:
            mid=(r+l)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            elif target < matrix[mid][0]:
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(matrix[0])-1
        while l<=r:
            mid_c=(r+l)//2
            if target == matrix[mid][mid_c]:
                return True
            elif target < matrix[mid][mid_c]:
                r=mid_c-1
            else:
                l=mid_c+1
        return False
        


        