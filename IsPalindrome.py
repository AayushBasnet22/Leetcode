class Solution:
    def isPalindrome(self, x: int) -> bool:
        num  = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x = x // 10
        if rev == num:
            return True
        else:
            return False