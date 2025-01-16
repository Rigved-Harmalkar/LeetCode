class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       left = 0
       right = 0
       res = ""
       if len(s) <=0:
        return True
       for char in t:
            if char == s[left]:
                res += char
                left += 1
            if len(res) == len(s):
                break
       return res == s
            




        