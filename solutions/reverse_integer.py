class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            result = int(str(x)[::-1])
        elif x < 0:
            result = -1 * int(str(x)[1:][::-1])
        else:
            return 0

        if -(2 ** 31) <= result <= 2 ** 31 - 1:
            return result
        else:
            return 0


if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(0) == 0
