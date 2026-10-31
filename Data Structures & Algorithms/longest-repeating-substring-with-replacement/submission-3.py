class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = 0
        chars = {}
        maxSize = 0
        
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0) + 1
            maxFreq = max(maxFreq, chars[s[right]])

            while (right - left + 1) - maxFreq > k:
                chars[s[left]] -= 1
                left += 1

            maxSize = max(maxSize, right - left + 1)

        return maxSize