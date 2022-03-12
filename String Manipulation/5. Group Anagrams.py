class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_anagrams = ["".join(sorted(list(string))) for string in strs]
        
        index_dict = {}
        for idx, string in enumerate(sorted_anagrams):
            if string not in index_dict:
                index_dict[string] = [idx]
            else:
                index_dict[string].append(idx)
        
        output = [list(map(strs.index, value)) for value in index_dict.values()]
        return output

solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs)
print(f"{result}")