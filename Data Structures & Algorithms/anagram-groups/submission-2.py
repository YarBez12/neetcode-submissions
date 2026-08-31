class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strToAnagrams = defaultdict(list)
        for s in strs:
            curr = "".join(sorted(s))
            strToAnagrams[curr].append(s)
        # ans = []
        # for k, v in strToAnagrams:
        #     ans.append(v)
        return list(strToAnagrams.values())
        