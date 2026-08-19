class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum=nums[0]
        minsum=nums[0]
        curmax=0
        curmin=0
        total=0
        for i in nums:
            total+=i
            curmax=max(0,curmax)+i
            maxsum=max(maxsum,curmax)

            curmin=min(0,curmin)+i
            minsum=min(minsum,curmin)

        if maxsum<0:
            return maxsum
            
        return max(maxsum,total-minsum)


        
        