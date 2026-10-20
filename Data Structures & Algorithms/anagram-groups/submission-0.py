class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for i in strs:
            sortedword = ''.join(sorted(i))
            if sortedword in my_dict:
                my_dict[sortedword].append(i)
            else:
                my_dict[sortedword] = [i]
        return list(my_dict.values())