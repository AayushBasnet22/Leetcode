class Solution:
    def strStr(self, haystack: str, needle: str) -> int: # 28 
        if needle in haystack:
            for index in range(len(haystack)):
                if haystack[index:index+len(needle)] == needle:
                    return index
        else:
            return -1