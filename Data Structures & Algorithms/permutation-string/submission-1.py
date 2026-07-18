class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp=self.getmap(s1)
        l=0
        r=len(s1)
        while r<len(s2)+1:
            if self.getmap(s2[l:r])==mapp:
                return True
            l+=1
            r+=1

        return False

    def getmap(self, s:str)->list:
        mapp=[0]*26
        for c in s:
            mapp[ord(c)-ord('a')]+=1
        return mapp

        