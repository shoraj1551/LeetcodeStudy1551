from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        A = Counter(s)
        B = Counter(t)
        for char in B:
            if B[char] != A.get(char, 0):
                return char
            
# Example usage:
s = "abcd"
t = "abcde"
solution = Solution()
result = solution.findTheDifference(s, t)
print(result)  # Output: e