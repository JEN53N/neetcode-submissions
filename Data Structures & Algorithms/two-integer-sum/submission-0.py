class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,j in enumerate(nums):
            total=target-j
            if total in dic:
                return [dic[total],i]
            
            dic[j]=i
     
