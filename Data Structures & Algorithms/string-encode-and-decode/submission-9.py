class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for string in strs:
            ret += str(len(string)) + "#" + string
        print(ret)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        left = 0
        length = ""
        while left < len(s):
            if s[left] != '#':
                length += s[left]
                left += 1
            else:
                ret.append(s[(left + 1):int(length) + left + 1])
                left = left + int(length) + 1
                length = ""
        return ret
        