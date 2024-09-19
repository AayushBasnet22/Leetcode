class Solution:
    def lenghtofLastWord(self, s: str) -> int:
        s = s[::-1]
        length = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if length == 0:
                    continue
                else:
                    break
            else:
                length += 1
        return length

