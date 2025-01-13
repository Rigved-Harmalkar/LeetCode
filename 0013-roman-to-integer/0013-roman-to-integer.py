class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for a, b in zip(s, s[1:]):
            if roman_char[a] < roman_char[b]:
                res -= roman_char[a]
            else:
                res += roman_char[a]

        return res + roman_char[s[-1]] 