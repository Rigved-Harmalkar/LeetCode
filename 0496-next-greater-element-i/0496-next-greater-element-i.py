class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        res = {}

        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1] < nums2[i]:
                st.pop()
            res[nums2[i]] = st[-1] if st else -1
            st.append(nums2[i])
        return [res[num] for num in nums1]

        

        