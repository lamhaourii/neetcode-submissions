class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs= [tuple(sorted(self.freq(s).items())) for s in strs]
        track={}
        for i,frq in enumerate(freqs):
            if frq in track.keys():
                track[frq].append(strs[i])
            else:
                track[frq]=[strs[i]]
        return list(track.values())

    def freq(self, s:str)->dict:
        t= {}
        for char in s:
            if char in t.keys():
                t[char]+=1
            else:
                t[char]=1
        return t