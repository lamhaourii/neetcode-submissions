class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1=self.track(s)
        map2=self.track(t)
        return map1==map2
    def track(self, s:str)->dict:
        mapT={}
        for char in s:
            if char in mapT.keys():
                mapT[char]+=1
            else:
                mapT[char]=1
        return mapT

        
        