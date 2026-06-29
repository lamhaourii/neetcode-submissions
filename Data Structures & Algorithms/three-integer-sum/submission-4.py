class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        lenght= len(nums)
        out=[]
        mapp={}
        for i in range(lenght):
            lbaqi= 0-nums[i]
            left= i+1
            right= lenght-1
            while left<right:
                if nums[left]+nums[right]<lbaqi:
                    left+=1
                elif nums[left]+nums[right]>lbaqi:
                    right-=1
                else:
                    to_check= [nums[i],nums[left],nums[right]]
                    tupl= tuple(to_check)
                    if mapp.get(tupl, 0)>0:
                        pass
                    else:
                        mapp[tupl]=1
                        out.append(to_check)

                    left+=1
                    right-=1
        return out



        