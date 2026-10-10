class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits)-1
        while carry and i >= 0:
            if digits[i] != 9:
                digits[i] += carry
                carry = 0
                break
            digits[i] = 0
            i -= 1
        return digits if not carry else [1] + digits
        