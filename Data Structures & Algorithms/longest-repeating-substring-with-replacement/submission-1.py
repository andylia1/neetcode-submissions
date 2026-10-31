class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        #for chr in s:
        #    count[chr] = count.get(chr, 0) + 1
        

        left = 0
        maxFreq = 0
        maxLen = 0

        # I need to find the max frequency of values in my window
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count.get(s[right], 0))

            while (right - left + 1) - maxFreq > k:
                count[s[left]] = count.get(s[left], 0) - 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
            print(maxLen)

            
                
        return maxLen