class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}

        for ball in range(lowLimit, highLimit + 1):
            # Calculate sum of digits
            x = ball
            digit_sum = 0

            while x > 0:
                digit_sum += x % 10
                x //= 10

            # Put ball into its box
            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1

        return max(boxes.values())