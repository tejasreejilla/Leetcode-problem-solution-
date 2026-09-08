class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(m):
            for c in range(n):
                live_neighbors = 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        # 1  = originally alive
                        # -1 = originally alive, but will die
                        if board[nr][nc] in (1, -1):
                            live_neighbors += 1

                # Currently alive
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  # 1 -> 0

                # Currently dead
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 2   # 0 -> 1

        # Convert temporary states to final states
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1
