class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        word_len = len(word)

        for s in strs[1:]:
            while word != s[0:word_len]:
                word_len -= 1
                if word_len == 0:
                    return ""
                
                word = word[0:word_len]

        return word

