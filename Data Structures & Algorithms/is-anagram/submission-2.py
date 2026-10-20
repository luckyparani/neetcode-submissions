class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}
        if len(s) == len(t):
            for ch in s :
                if ch not in mydict :
                    mydict[ch] = 1 
                else:
                    mydict[ch] += 1 
            for ch in t :
                if ch not in mydict :
                    return False 
                    break 
                else:
                    mydict[ch] -= 1 
            for k , v in mydict.items():
                if v != 0 :
                    return False 
                    break 
            return  True 
        else:
            return False                           


            
        