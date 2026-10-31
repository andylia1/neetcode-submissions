class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = defaultdict(int)
        chars_t = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            chars_s[s[i]] = chars_s[s[i]] + 1
            chars_t[t[i]] = chars_t[t[i]] + 1

        if chars_s == chars_t:
            return True

        return False
