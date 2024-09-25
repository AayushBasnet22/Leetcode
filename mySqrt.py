class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            sqrt = (left + right) // 2
            if sqrt * sqrt < x:
                left = sqrt + 1
            elif sqrt * sqrt > x:
                right = sqrt -1
            else:
                return sqrt
        return right
