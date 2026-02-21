class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            if self.isPrime(bin(i)[2:].count('1')):
                count+=1
        return count
    
    def isPrime(self, x):
        if x<=1:
            return False
        if x==2:
            return True
        if x%2==0:
            return False
        
        for i in range(3, int(math.sqrt(x))+1, 2):
            if x%i==0:
                return False
        return True