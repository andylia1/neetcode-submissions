class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        uniques = set()

        for right in range(len(s)):
            while s[right] in uniques:
                uniques.remove(s[left])
                left += 1
            uniques.add(s[right])
            maxLen = max(maxLen, len(uniques))



        return maxLen
