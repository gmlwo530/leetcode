class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0

        len_max = 0

        tmp_li = []

        for c in s:
            try:
                same_c_index = tmp_li.index(c)

                tmp_li.append(c)
                tmp_li = tmp_li[same_c_index + 1 :]

                if len(tmp_li) > len_max:
                    len_max = len(tmp_li)
            except ValueError:
                tmp_li.append(c)
                if len(tmp_li) > len_max:
                    len_max = len(tmp_li)

        return len_max


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
