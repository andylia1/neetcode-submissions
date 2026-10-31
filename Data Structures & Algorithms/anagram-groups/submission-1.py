class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a dict of dicts of anagrams
        ret = defaultdict(list)

        for string in strs:
            alphabet = [0] * 27
            for ch in string:
                alphabet[ord(ch) - ord('a')] += 1
            ret[tuple(alphabet)].append(string)
        return list(ret.values())
