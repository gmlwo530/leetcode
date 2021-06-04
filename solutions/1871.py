class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # if s[-1] == "1" or "0" not in s[len(s) - maxJump - 2 : len(s) - 1]:
        #     return False

        if s[-1] == "1":
            return False

        i = 0
        while True:
            if s[i] == "0":
                if "0" in s[i + minJump : i + maxJump + 1]:
                    if i + maxJump + 1 == len(s):
                        return True
                    continue
                else:
                    return False

        for i, c in enumerate(s[:-1]):
            if c == "0":
                if "0" in s[i + minJump : i + maxJump + 1]:
                    if i + maxJump + 1 == len(s):
                        return True
                    continue
                else:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canReach("011010", 2, 3)
    assert s.canReach("01101100", 2, 4)
    assert not s.canReach("01101110", 2, 3)
