class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        uniques = set()
        maxLen = 0

        for right in range(len(s)):
            while uniques and s[right] in uniques:
                uniques.remove(s[left])
                left += 1
            uniques.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
            