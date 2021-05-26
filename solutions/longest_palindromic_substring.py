class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        len_s = len(s)
        result = s[0]

        for tl in range(len_s, 1, -1):
            for i in range(len_s - tl + 1):
                if s[i : i + tl] == s[i : i + tl][::-1]:
                    result = s[i : i + tl]
                    break
            else:
                continue
            break

        return result


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
