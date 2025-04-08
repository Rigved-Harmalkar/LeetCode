class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dictt = {}
        max_len = 0

        for right, char in enumerate(s):
            dictt[char] = 1 + dictt.get(char,0)
            while dictt[char] > 1:
                dictt[s[left]] -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len