class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars= set(s)
        res=0
        for char in chars:
            l=0
            r=0
            v=k
            last=0
            for r in range(len(s)):
                if s[r]!=char:
                    v-=1
                    
                while v<0 and l<len(s):
                    res=max(res,r-l)
                    if s[l]!=char:
                        v+=1
                    l+=1
            if r==len(s)-1:
                res=max(res,r-l+1)
                    

                


        return res
                        

                    





        



        