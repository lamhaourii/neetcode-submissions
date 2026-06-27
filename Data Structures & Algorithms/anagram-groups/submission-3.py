class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track={}
        for s in strs:
            frq=tuple(self.freq(s))
            if frq in track.keys():
                track[frq].append(s)
            else:
                track[frq]=[s]
        return list(track.values())

    def freq(self, s:str)->dict:
        t= [0]*26
        for char in s:
            t[ord(char)-ord('a')]+=1
        return t