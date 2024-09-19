class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        max_length, left = 0, 0
        for right in range(len(s)):
            if s[right] not in characters:
                characters.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in characters:
                    characters.remove(s[left])
                    left += 1
                characters.add(s[right])
        return max_length
        