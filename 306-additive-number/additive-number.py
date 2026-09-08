class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        # Add two non-negative integers represented as strings.
        def add(a: str, b: str) -> str:
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:
                x = int(a[i]) if i >= 0 else 0
                y = int(b[j]) if j >= 0 else 0

                total = x + y + carry
                result.append(str(total % 10))
                carry = total // 10

                i -= 1
                j -= 1

            return ''.join(reversed(result))

        n = len(num)

        # Choose the first number num[0:i]
        for i in range(1, n):

            # First number cannot have leading zero
            if num[0] == '0' and i > 1:
                break

            # Choose the second number num[i:j]
            for j in range(i + 1, n):

                # Second number cannot have leading zero
                if num[i] == '0' and j - i > 1:
                    break

                first = num[:i]
                second = num[i:j]

                # We need at least one more number.
                remaining = j
                count = 2

                while remaining < n:
                    third = add(first, second)

                    # The next number must match exactly.
                    if not num.startswith(third, remaining):
                        break

                    remaining += len(third)
                    first, second = second, third
                    count += 1

                # Entire string was consumed and we have >= 3 numbers.
                if remaining == n and count >= 3:
                    return True

        return False

