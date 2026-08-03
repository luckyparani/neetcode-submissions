class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old_person = 0 
        for person in details:
            age = int(person[11])*10 + int(person[12])
            if age > 60 :
                old_person += 1 
        return old_person        
        