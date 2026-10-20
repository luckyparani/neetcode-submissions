class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com = {}
        for i in range (len(nums)):
            c = target - nums[i] 
            if c in com:
                return [com[c] , i]    
                break   
            com[nums[i]] = i     
            
              
             
            
        