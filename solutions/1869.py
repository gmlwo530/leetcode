class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_one = 0
        max_zero = 0
        curr_one = 0
        curr_zero = 0
        prev = None

        dummy_c = "1" if s[-1] == "0" else "0"

        for c in s + dummy_c:
            if prev and prev != c:
                if c == "1":
                    max_zero = max(max_zero, curr_zero)
                    curr_zero = 0
                else:
                    max_one = max(max_one, curr_one)
                    curr_one = 0

            if c == "1":
                curr_one += 1
            else:
                curr_zero += 1

            prev = c

        return max_one > max_zero


if __name__ == "__main__":
    s = Solution()
    assert s.checkZeroOnes("1101")
    assert s.checkZeroOnes("1111")
    assert not s.checkZeroOnes("10")
    assert not s.checkZeroOnes("1010")
    assert not s.checkZeroOnes("0000")
    assert not s.checkZeroOnes("111000")
    assert not s.checkZeroOnes("110100010")
    assert s.checkZeroOnes("0111010011")
