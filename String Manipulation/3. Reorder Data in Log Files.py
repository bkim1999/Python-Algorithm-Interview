class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letters = [log for log in logs if log.split()[1].isalpha()]
        digits = [log for log in logs if log.split()[1].isdigit()]
        
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits

solution = Solution()
input1 = logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
result = solution.reorderLogFiles(input1)
print(f"{result}")