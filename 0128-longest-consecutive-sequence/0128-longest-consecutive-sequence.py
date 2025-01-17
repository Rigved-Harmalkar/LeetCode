class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        n = len(a)
        max_count = 1
        count = 1
        if n == 0:
            return 0

        elements = set()

        for ele in a:
            elements.add(ele)

        for ele in elements:
            count = 1
            if ele - 1 not in elements:
                x = ele
                while x + 1 in elements:
                    count += 1
                    x = x + 1
                    max_count = max(max_count,count)
        return max_count