from collections import OrderedDict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        lenght=0
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
                lenght+=1
        sorted_freq = OrderedDict(sorted(freq.items(), key=lambda item: item[1]))
        return list(sorted_freq.keys())[lenght-k:]
        
        