class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1:
            return True
        hand.sort()
        d = defaultdict(list)
        for card in hand:
            if card-1 not in d or not d[card-1]:
                d[card].append(groupSize - 1)
                continue
            i = d[card-1].pop()
            if i > 1:
                d[card].append(i-1)
        for k, v in d.items():
            if v:
                return False
        return True
        