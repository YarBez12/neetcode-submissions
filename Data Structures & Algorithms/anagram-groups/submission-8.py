class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strToAnagrams = defaultdict(list)
        for s in strs:
            curr = "".join(sorted(s))
            # count = [0] * 26
            # for c in s:
            #     count[ord(c) - ord('a')] += 1
            # strToAnagrams[tuple(count)].append(s)
            strToAnagrams[curr].append(s)
        return list(strToAnagrams.values())
        