class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = target[:]
        for triplet in triplets:
            copy = t[:]
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    copy = None
                    break
                if triplet[i] == target[i]:
                    copy[i] = -1
            if copy:
                t = copy
        return all(x == -1 for x in t)