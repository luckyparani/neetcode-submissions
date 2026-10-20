class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        output = []
        for i in nums:
            if i in my_dict:
                my_dict[i] += 1 
            else:
                my_dict[i] = 1 
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))   
        while k !=0 :
            last , _ = (sorted_dict.popitem())
            output.append(last)
            k -= 1
        return output

          

            


       

                     
        