class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = "".join([char for char in s if char.isalnum()]).lower()
        s_len = len(s_lower)
        if s_len % 2 == 0:
            return s_lower[:s_len//2] == s_lower[:s_len//2-1:-1]
        else:
            return s_lower[:s_len//2] == s_lower[:s_len//2:-1]

solution = Solution()
if solution.isPalindrome(input()): print("True")
else: print("False")