class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i, num in enumerate(nums):
            
            rest= target-num
            if rest in track.keys():
                return [track[rest],i]    
            track[num]=i        

        