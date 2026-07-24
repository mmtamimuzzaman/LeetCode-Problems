class Solution:
    def threeSum(self, nums):
        for i in range(len(nums)):
            target = -nums[i]
            items = {}
            for j in range(i+1,len(nums)):
                needed = target - nums[j]
                if needed in items:
                    return [nums[i],nums[j],needed]
                items[nums[j]] = j


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))        
        