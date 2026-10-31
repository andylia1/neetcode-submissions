class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_words = {}
        t_words = {}

        for i in range(len(s)):
            s_words[s[i]] = s_words.get(s[i], 0) + 1
            t_words[t[i]] = t_words.get(t[i], 0) + 1
        if s_words == t_words:
            return True
        return False
        