class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()
        maxLen = 0

        for right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1
                window.add(s[right])
            maxLen = max(maxLen, len(window))



        return maxLen
