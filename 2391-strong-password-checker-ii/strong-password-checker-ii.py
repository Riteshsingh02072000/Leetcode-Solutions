class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        low, upp, spe, dig = 0,0,0,0
        
        for i in range(len(password)):
            if i!=0 and password[i]==password[i-1]:
                return False
            elif 65<=ord(password[i])<=90:
                low+=1
            elif 97<=ord(password[i])<=122:
                upp+=1
            elif 48<=ord(password[i])<=57:
                dig+=1
            else:
                spe+=1
        if low>0 and upp>0 and dig>0 and spe>0:
            return True
        return False
            