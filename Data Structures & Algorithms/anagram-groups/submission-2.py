class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dict of dicts of anagrams
        anagrams = defaultdict(list)

        for string in strs:
            key = [0] * 26

            for ch in string:
                key[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(key)].append(string)
        
        return list(anagrams.values())


