class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lenght= len(nums)
        left_mult= [nums[0]]
        right_mult=[nums[-1]]
        for i in range(1, lenght-1):
            left_mult.append(left_mult[i-1]* nums[i])
        for i in range(1, lenght-1):
            right_mult.append(right_mult[i-1]*nums[-i-1])
        out=[1]*lenght
        out[0]=right_mult[-1]
        out[-1]=left_mult[-1]
        for i in range(lenght-2):
            out[i+1]= left_mult[i]*right_mult[lenght-3-i]

        return out

        
        

        