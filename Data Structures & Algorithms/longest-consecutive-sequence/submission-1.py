class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mapp={}
        longest=1
        for num in nums:
            if mapp.get(num):
                pass
            else:
                mapp[num]=1   

        for num in mapp.keys():
            current_long=1
            current=num-1
            while mapp.get(current, 0)==1:
                current_long+=1
                current -=1
            if current_long >longest:
                longest=current_long
        return longest

            
    

              