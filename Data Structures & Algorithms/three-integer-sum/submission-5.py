class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        lenght= len(nums)
        out=[]
        for i in range(lenght):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lbaqi= 0-nums[i]
            left= i+1
            right= lenght-1
            while left<right:
                if left >i+1 and nums[left]==nums[left-1]:
                    left +=1
                    continue
                if right < lenght-1 and nums[right]==nums[right+1]:
                    right -=1
                    continue
                
                if nums[left]+nums[right]<lbaqi:
                    left+=1
                elif nums[left]+nums[right]>lbaqi:
                    right-=1
                else:
                    
                    out.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
        return out



        