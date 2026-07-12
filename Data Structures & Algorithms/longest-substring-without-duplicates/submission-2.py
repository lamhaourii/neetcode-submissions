class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        unique=[s[0]]
        lp=0
        rp=1
        min_s=1
        while rp<len(s):
            if s[rp] not in unique:
                unique.append(s[rp])
                rp+=1
            else:
                del unique[0]
                lp+=1
            if len(unique)>min_s:
                min_s=len(unique)
        return min_s








        