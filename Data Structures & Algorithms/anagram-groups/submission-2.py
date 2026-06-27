class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        track={}
        for s in strs:
            frq=tuple(sorted(self.freq(s).items()))
            if frq in track.keys():
                track[frq].append(s)
            else:
                track[frq]=[s]
        return list(track.values())

    def freq(self, s:str)->dict:
        t= {}
        for char in s:
            if char in t.keys():
                t[char]+=1
            else:
                t[char]=1
        return t