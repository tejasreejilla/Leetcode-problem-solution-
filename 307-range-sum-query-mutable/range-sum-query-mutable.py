class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        # Build Fenwick Tree
        for i, value in enumerate(nums):
            self._add(i + 1, value)

    def _add(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def _prefix_sum(self, index: int) -> int:
        total = 0

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]

        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)

