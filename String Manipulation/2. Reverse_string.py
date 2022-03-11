class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

solution = Solution()
s = list(input())
solution.reverseString(s)
print(f"{s}")