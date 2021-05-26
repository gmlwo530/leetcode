class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        i, l = 0, 0
        for j in range(len(s)):
            # 저장된 l보다 1이 더 큰 길이에 대해서 검사.
            if s[j - l : j + 1] == s[j - l : j + 1][::-1]:
                i, l = j - l, l + 1
            elif j - l > 0 and s[j - l - 1 : j + 1] == s[j - l - 1 : j + 1][::-1]:
                i, l = j - l - 1, l + 2

        return s[i : i + l]


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ac") == "a"
    assert s.longestPalindrome("cbdc") == "c"
    assert s.longestPalindrome("cbdccazyxcccadb") == "ccc"
    assert s.longestPalindrome("cbdcbdcbdcbdcbdcbdcbdcbdcbd") == "c"
    assert s.longestPalindrome("abbdefghijklmnopqrstuxyz") == "bb"
