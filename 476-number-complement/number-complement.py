class Solution:
    def findComplement(self, num: int) -> int:
        def decBin(n):
            return bin(n)[2:]
        
        def binDec(binary):
            decimal = 0
            cur= 0

            for i in  range(len(binary)-1, -1, -1):
                decimal += int(binary[i])*(2**cur)
                cur+=1
            return decimal
        # print(bin)
            
        binary = decBin(num)
        n = len(binary)
        ans = ''

        for i in range(n):
            if binary[i] == '1':
                ans += '0'
            else:
                ans+='1'
        return binDec(ans)