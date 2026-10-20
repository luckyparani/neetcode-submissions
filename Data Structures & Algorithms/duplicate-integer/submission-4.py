class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = sorted(nums)
        # i = 0 
        # flag = False

        # for i in range(len(nums)-1):
        #     j = i+1
        #     if nums[i] == nums[j]:
        #         flag = True
        #         break 
        # return flag    
        #________________________________________
        if len(nums) == len(set(nums)):
            return False
        else:
            return True  
        #_________________________________________
        # my_dict = dict()
        # for i in nums:
        #     if i in my_dict:
        #         my_dict[i] += 1
        #     else:
        #         my_dict[i] = 1 
        # for key,value in my_dict.items():
        #     if value > 1 :
        #         return True 
        # return False                

        