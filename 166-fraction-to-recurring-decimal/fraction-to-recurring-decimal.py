class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if denominator == 0:
            return ""
        
        ans  =""

        if (numerator<0) ^ (denominator<0):
            ans += '-'
        
        numerator, denominator = abs(numerator), abs(denominator)
    
        ans += str(numerator//denominator)

        if numerator%denominator==0:
            return ans
        
        ans += '.'
        dic = {}
        remd = numerator%denominator

        while remd!=0 and remd not in dic:
            dic[remd] = len(ans)
            remd*=10
            ans += str(remd//denominator)
            remd%=denominator
        
        if remd in dic:
            ans=  ans[:dic[remd]] + '(' + ans[dic[remd]:] + ')'
        
        return ans