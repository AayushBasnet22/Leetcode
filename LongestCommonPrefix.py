class Solution:
     def longestCommonPrefix(self, strs: list[str]) -> str: 
        common_string=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return common_string
            common_string+=first[i]
        return common_string 