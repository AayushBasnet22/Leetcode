class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a , b = map(int,[a,b])
        sum_string = str(a + b)
        final_sum = ''
        c = 0
        for s in sum_string[::-1]:
            if c + int(s) == 0:
                c = 0
                final_sum += '0'
            elif c + int(s) == 1:
                c = 0
                final_sum += '1'
            elif c + int(s) == 2:
                c = 1
                final_sum += '0'
            else:
                c = 1
                final_sum += '1'
        return '1' + final_sum[::-1] if c == 1 else final_sum[::-1]