class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0

        secret_count = [0] * 10
        guess_count = [0] * 10

        # First, find bulls and count non-bull digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[int(s)] += 1
                guess_count[int(g)] += 1

        # Count cows
        cows = 0
        for digit in range(10):
            cows += min(secret_count[digit], guess_count[digit])

        return f"{bulls}A{cows}B"

