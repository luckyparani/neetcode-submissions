class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my_list =s.split()
        n = len(my_list)-1 
        count = 0 
        for i in my_list[n]:
            count+= 1
        return count     


        