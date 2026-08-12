class Solution:
    def addOperators(self, num, target):
        result = []

        def dfs(index, expression, value, prev):
            # We've used all digits
            if index == len(num):
                if value == target:
                    result.append(expression)
                return

            # Try every possible next number
            for end in range(index, len(num)):
                # No leading zeros
                if end > index and num[index] == '0':
                    break

                current_str = num[index:end + 1]
                current = int(current_str)

                # First number
                if index == 0:
                    dfs(
                        end + 1,
                        current_str,
                        current,
                        current
                    )
                else:
                    # +
                    dfs(
                        end + 1,
                        expression + "+" + current_str,
                        value + current,
                        current
                    )

                    # -
                    dfs(
                        end + 1,
                        expression + "-" + current_str,
                        value - current,
                        -current
                    )

                    # *
                    dfs(
                        end + 1,
                        expression + "*" + current_str,
                        value - prev + prev * current,
                        prev * current
                    )

        dfs(0, "", 0, 0)

        return result