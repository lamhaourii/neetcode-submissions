class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mapp=self.getmap(s1)
        l=0
        r=len(s1)
        mapp2=self.getmap(s2[l:r])
        while r<len(s2)+1:
            
            if mapp2==mapp:
                return True
            mapp2[ord(s2[l])-ord('a')]-=1
            if r<len(s2):
                mapp2[ord(s2[r])-ord('a')]+=1
            l+=1
            r+=1

        return False

    def getmap(self, s:str)->list:
        mapp=[0]*26
        for c in s:
            mapp[ord(c)-ord('a')]+=1
        return mapp

        