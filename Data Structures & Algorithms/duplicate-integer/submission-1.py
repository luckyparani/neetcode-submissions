class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        i = 0 
        flag = False

        for i in range(len(nums)-1):
            j = i+1
            if nums[i] == nums[j]:
                flag = True
                break 
        return flag    


        