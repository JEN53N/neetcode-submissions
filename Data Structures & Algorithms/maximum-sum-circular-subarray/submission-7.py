class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum=nums[0]
        minsum=nums[0]
        cursum=0
        curmin=0
        total=0

        for i in nums:
            total+=i
            cursum=max(0,cursum)+i
            maxsum=max(maxsum,cursum)

            curmin=min(0,curmin)+i
            minsum=min(minsum,curmin)

        while maxsum<0:
            return maxsum
        return max(maxsum,total-minsum)



        
        