class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(start, end):
            while 0 <= start < len(s) and 0 <= end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]

        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key = len)
        return result

solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(f"{result}")