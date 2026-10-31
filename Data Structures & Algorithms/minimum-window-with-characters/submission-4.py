class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        minLen = float('infinity')
        have = 0
        left = 0
        countT = {}
        countS = {}
        minIndex = [0, 0]

        for chr in t:
            countT[chr] = countT.get(chr, 0) + 1
            countS[chr] = 0
 
        for right in range(len(s)):
        
            if s[right] in countT:
                countS[s[right]] += 1
                if countS[s[right]] == countT[s[right]]:
                    have += 1

            while have == len(countT):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    minIndex = [left, right + 1]
                if s[left] in countT:
                    countS[s[left]] -= 1
                    if countS[s[left]] < countT[s[left]]:
                        have -= 1
                left += 1
            
        if minLen != float('infinity'):
            return s[minIndex[0] : minIndex[1]] 
        else:
            return ""
        
        
            


            



                
            


           


    
        

        