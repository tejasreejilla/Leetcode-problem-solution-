class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Find the first character appearing once
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        return -1