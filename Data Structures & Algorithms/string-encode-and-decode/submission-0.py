class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return str(chr(258))
        return chr(257).join(strs)

    def decode(self, s: str) -> List[str]:
        if s == str(chr(258)):
            return []
        return s.split(chr(257))
