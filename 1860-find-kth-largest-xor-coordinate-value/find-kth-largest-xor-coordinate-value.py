import heapq

class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        # prefix[i][j] = XOR of matrix[0:i][0:j]
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        values = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    prefix[i - 1][j]
                    ^ prefix[i][j - 1]
                    ^ prefix[i - 1][j - 1]
                    ^ matrix[i - 1][j - 1]
                )

                values.append(prefix[i][j])

        # kth largest
        return heapq.nlargest(k, values)[-1]