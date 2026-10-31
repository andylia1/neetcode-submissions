class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        have = 0
        t_char = {}
        s_char = {}
        ret = ""
        minLen = float('infinity')
        

        for chr in t:
            t_char[chr] = t_char.get(chr, 0) + 1
            s_char[chr] = 0

        for right in range(len(s)):
            if s[right] in t_char:
                s_char[s[right]] += 1
                if s_char[s[right]] == t_char[s[right]]:
                    have += 1
            

            while left <= right and have == len(t_char.keys()):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    ret = s[left:right + 1]

                    
                if s[left] in t_char:
                    s_char[s[left]] -= 1
                    if s_char[s[left]] == t_char[s[left]] - 1:
                        have -= 1
                left += 1
            
        return ret
