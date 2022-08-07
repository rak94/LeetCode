class PalindromicSubstrings:
    def substrings(self, s: str) -> int:
        res = 0

        for idx in range(len(s)):
            left = right = idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
            
            left = idx
            right = idx + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res