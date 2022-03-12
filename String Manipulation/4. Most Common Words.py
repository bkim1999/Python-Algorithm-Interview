import re, collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        pattern = re.compile('[\w]+')
        words = [word.lower() for word in pattern.findall(paragraph) if word.lower() not in banned]
        words_counter = collections.Counter(words)
        return words_counter.most_common(1)[0][0]

solution = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
result = solution.mostCommonWord(paragraph, banned)
print(f"{result}")