class Solution:
    def romanToInt(self,s: str) -> int:
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        number = 0
        if len(s) == 1:
            return d[s[0]]
        else:
            for i in range(len(s)-1):
                if d[s[i]] < d[s[i+1]]:
                    number -= d[s[i]]
                else:
                    number += d[s[i]]  
            number += d[s[i+1]]
            return number