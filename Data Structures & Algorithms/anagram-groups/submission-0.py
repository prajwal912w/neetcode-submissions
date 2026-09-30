class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            joined = "".join(sorted(word))

            if joined not in anagrams:
                anagrams[joined] = []

            anagrams[joined].append(word)

        return list(anagrams.values())
