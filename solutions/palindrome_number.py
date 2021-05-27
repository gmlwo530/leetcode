class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1] if x >= 0 else False


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121)
    assert not s.isPalindrome(-121)
    assert not s.isPalindrome(10)
    assert not s.isPalindrome(-101)
    assert s.isPalindrome(0)
