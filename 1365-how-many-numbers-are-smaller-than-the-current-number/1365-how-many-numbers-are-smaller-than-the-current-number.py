class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            a = 0
            for j in nums:
                if j<i:
                    a+=1
            ans.append(a)
        return ans

