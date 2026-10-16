class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        start = end = 0
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        for i in range(len(s)):
            for left, right in (expand(i, i), expand(i, i + 1)):
                if right - left > end - start:
                    start, end = left, right
        return s[start:end + 1]
