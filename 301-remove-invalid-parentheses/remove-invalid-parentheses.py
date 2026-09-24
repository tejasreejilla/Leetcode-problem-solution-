class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Find the minimum number of '(' and ')' to remove.
        left_remove = right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def dfs(index, path, balance, left_rem, right_rem):
            # Invalid prefix
            if balance < 0:
                return

            # Reached the end
            if index == len(s):
                if balance == 0 and left_rem == 0 and right_rem == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            if ch == '(':
                # Option 1: remove this '('
                if left_rem > 0:
                    dfs(
                        index + 1,
                        path,
                        balance,
                        left_rem - 1,
                        right_rem
                    )

                # Option 2: keep this '('
                path.append(ch)
                dfs(
                    index + 1,
                    path,
                    balance + 1,
                    left_rem,
                    right_rem
                )
                path.pop()

            elif ch == ')':
                # Option 1: remove this ')'
                if right_rem > 0:
                    dfs(
                        index + 1,
                        path,
                        balance,
                        left_rem,
                        right_rem - 1
                    )

                # Option 2: keep this ')'
                if balance > 0:
                    path.append(ch)
                    dfs(
                        index + 1,
                        path,
                        balance - 1,
                        left_rem,
                        right_rem
                    )
                    path.pop()

            else:
                # Letters are always kept
                path.append(ch)
                dfs(
                    index + 1,
                    path,
                    balance,
                    left_rem,
                    right_rem
                )
                path.pop()

        dfs(0, [], 0, left_remove, right_remove)

        return list(result)