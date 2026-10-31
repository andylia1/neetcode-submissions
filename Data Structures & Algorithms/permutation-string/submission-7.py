class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1


        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            rightInd = ord(s2[right]) - ord('a')
            leftInd = ord(s2[left]) - ord('a')

            #Handle right case
            count2[rightInd] += 1
            if count2[rightInd] == count1[rightInd]:
                matches += 1
            elif count2[rightInd] == count1[rightInd] + 1:
                matches -= 1

            #Handle left case
            count2[leftInd] -= 1
            if count2[leftInd] == count1[leftInd]:
                matches += 1
            elif count2[leftInd] == count1[leftInd] - 1:
                matches -= 1
            left += 1

        return matches == 26
            
            

            
            