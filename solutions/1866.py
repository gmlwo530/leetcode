"""
Reference: https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/discuss/1211097/Python-DP-O(n*k)-with-explanation%3A-insert-the-shortest-stick
"""  # noqa: E501

from functools import cache

M = 10 ** 9 + 7


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        return dp(n, k)


@cache
def dp(n: int, k: int) -> int:
    if n == k:
        return 1

    if n <= 0 or k <= 0:
        return 0

    return (dp(n - 1, k - 1) + (n - 1) * dp(n - 1, k)) % M


if __name__ == "__main__":
    s = Solution()

    assert s.rearrangeSticks(3, 2) == 3
    assert s.rearrangeSticks(5, 5) == 1
    assert s.rearrangeSticks(20, 11) == 647427950 % M
