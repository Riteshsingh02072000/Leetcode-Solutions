class Solution:
    def intToRoman(self, num: int) -> str:
        value = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'         
        }

        ans = ""
        for key, val in value.items():
            while num>=key:
                ans += value[key]
                num-=key
            if num == 0:
                return ans
        return ans