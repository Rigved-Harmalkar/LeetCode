class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        dictt = {}
        for i in range(len(arr)):
            if arr[i] not in dictt.keys():
                dictt[arr[i]] = 1
            else:
                dictt[arr[i]] += 1
                
        for k,v in dictt.items():
            if v == 1:
                return k
        return -1
        