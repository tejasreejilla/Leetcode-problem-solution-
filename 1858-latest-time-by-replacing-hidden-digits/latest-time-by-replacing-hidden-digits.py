class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)

        # Hour tens
        if t[0] == '?':
            t[0] = '2' if t[1] == '?' or t[1] <= '3' else '1'

        # Hour ones
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'

        # Minute tens
        if t[3] == '?':
            t[3] = '5'

        # Minute ones
        if t[4] == '?':
            t[4] = '9'

        return ''.join(t)