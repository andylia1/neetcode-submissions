class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        length = ""
        while i < len(s):
            if s[i] != '#':
                length += s[i]
                i += 1
            else:
                print(length)
                ret.append(s[i+1:int(length)+i + 1])
                i = i + int(length) + 1
                length = ""
        return ret
            
            

        