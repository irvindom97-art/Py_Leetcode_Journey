class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == " ": i += 1
        sign = 1
        if i < n and s[i] in "+-":
            if s[i] == "-": sign = -1
            i += 1
        number = 0
        while i < n and s[i].isascii() and s[i].isdigit():
            number = number * 10 + int(s[i])
            i += 1
        number *= sign
        return max(-(2**31), min(2**31 - 1, number))
