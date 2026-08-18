class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=0
        maxsum=nums[0]
        minsum=nums[0]
        cursum=0
        curmin=0
        for i in nums:
            total+=i
            cursum=max(0,cursum)+i
            maxsum=max(cursum,maxsum)          

            curmin=min(curmin,0)+i
            minsum=min(curmin,minsum)
        if maxsum<0:
            return maxsum
        return max(maxsum,total-minsum)
        