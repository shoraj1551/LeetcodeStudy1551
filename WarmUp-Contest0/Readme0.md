Question01: Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
 
Example 1:
Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:
Input: n = 2
Output: [1,2]
Constraints:
•	1 <= n <= 5 * 104

Solution: 
Lexicographical Order: Lexicographical order is similar to dictionary order, where strings are compared character by character. When applied to numbers, it means treating the numbers as strings and sorting them in dictionary order.
Example: Consider numbers from 1 to 13. Their lexicographical order would be:
1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
Because:
•	"1" < "10" < "11" < "12" < "13" < "2" < "3" ...
Note that this is not numerical order.
Why is it useful?
In Software Development:
1.	Autocomplete Systems:  Autocomplete needs to suggest the next possible string in lexicographical order (like search engine suggestions).
2.	File Systems: Files are often sorted alphabetically. Sorting file names like file1.txt, file10.txt, file2.txt requires lexicographical handling.
3.	Version Control: Semantic versioning tools (like v1.10.0 vs v1.2.0) use lexicographical and numerical combinations.
4.	Databases: Indexes based on keys are often sorted lexicographically (especially in NoSQL databases like Redis, Cassandra, etc.).
5.	Trie-based applications: Lexicographical ordering is a natural fit for tree structures (used in spell-check, prefix search, etc.).
6.	Pagination systems: Lex order can be used to paginate large sets of data when IDs are string-based or natural sort isn't desired.
In Real Life Use-Cases:
1.	Phonebook or Contact List Sorting: Names are sorted lexicographically.
2.	Digital Library Catalogs: Books, articles, or documents are often displayed in lexicographical order by title or ID.
3.	Airline Passenger List: Sorted by name in lexicographical order for boarding or check-in.
4.	E-commerce Filters: Product names/categories sorted lexicographically.
Code: 
class Solution:
def lexicalOrder(self, n: int) -> List[int]:
    		list_Int = [i+1 for i in range(n)]                        # O(n)
    		list_Str = sorted([str(i) for i in list_Int])             # O(n log n)
    		return [int(i) for i in list_Str]                         # O(n)

Performance Analysis:
•	Time Complexity: O(n log n) due to the sorting of strings.
•	Space Complexity: O(n) for storing all numbers and strings.
•	It uses extra memory to hold:
o	An integer list list_Int
o	A string list list_Str
•	Then reconverts back to integers — redundant and unnecessary.


Can it be Optimized? : Yes! You can eliminate sorting and extra memory by using a DFS-based traversal to generate numbers in lexicographical order on the fly.
 Key Idea: Start DFS from 1 to 9 (since 0 is invalid for our range), and for each number curr, explore curr * 10, curr * 10 + 1, ..., curr * 10 + 9 — but stop recursion when curr > n.

Optimized Code (DFS Approach)
def lexicalOrder(self, n: int) -> List[int]:
    result = []
    def dfs(curr):
        if curr > n:
            return
        result.append(curr)
        for i in range(10):
            next_num = curr * 10 + i
            if next_num > n:
                break
            dfs(next_num)
for i in range(1, 10):
        dfs(i)

    return result

Benefits of DFS Version:
Feature	Old Code	DFS Optimized Code
Time	O(n log n)	O(n) (each number visited once)
Space	O(n) + intermediate strings	O(n) (just the result)
Memory usage	High (2 extra lists)	Minimal (only result list)
Conversion overhead	Yes (int → str → int)	None

Real-World Impact
•	For n = 10⁵ or 10⁶, your original code becomes slow and memory-heavy due to sorting and conversions.
•	The DFS version scales linearly and avoids unnecessary overhead, making it production-grade.


Best Leet Code Solution Analysis:

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        number = 1
        for i in range(n):
            result.append(number)
            if number * 10 <= n:
                number *= 10
            else:
                if number >= n:
                    number //= 10
                number += 1
                while number % 10 == 0:
                    number //= 10
        return result
What This Code Does: It simulates a lexicographical traversal by constructing the next number based on prefix logic — without recursion.

Main Logic Flow:
1.	Start with number = 1.
2.	If number * 10 <= n:
→ go deeper (e.g., 1 → 10 → 100)
3.	Else:
o	If number >= n: backtrack (e.g., 199 → 20)
o	Else increment (e.g., 1 → 2 → 3)
o	If the new number ends in 0s, move up (e.g., 19 → 20 → 2)

Comparison Table
Feature	Original (Sort-based)	DFS (Recursive)	Iterative (This One)
Time Complexity	O(n log n)	O(n)	O(n)
Space (Auxiliary/Stack)	O(n) + str conversion	O(n) result + O(log n) stack	O(n) result only
Memory Efficient	❌	⚠️ (uses recursion)	✅ Yes
Recursion Depth Risk	❌	⚠️ Deep stack possible	✅ No recursion
Conversion Overhead	❌ Yes	✅ None	✅ None
Best for Very Large n	❌	⚠️ Stack overflow risk	✅ Most scalable and safe
Elegance	Moderate	Elegant but recursive	✅ Very concise and robust
________________________________________

Final Verdict: The iterative solution is:
•	As fast as the DFS solution,
•	More memory efficient (no recursion),
•	Safer for large inputs (no stack overflow),
•	Cleaner in logic once understood.

------------------------------------------------------------------------------------------------------------------------------------------------

Question02: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
 Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"	
Output: -1
Constraints:
•	1 <= s.length <= 105
•	s consists of only lowercase English letters.

Solutions:
ChatGPT Solution – 
class Solution(object):
 from collections import Counter
def firstUniqChar(self, s: str) -> int:
        	# Step 1: Count frequency of each character
        	freq = Counter(s)
# Step 2: Find the first character with count 1
        	for idx, char in enumerate(s):
            		if freq[char] == 1:
                		return idx
        return -1  # If no unique character exists

Metric	Value
Time	O(n)
Space	O(1) (26 chars max for lowercase letters)


Leet Code best solution- 

✅ Explanation of the Provided Code
class Solution:
    def firstUniqChar(self, s: str) -> int:
        key = 'abcdefghijklmnopqrstuvwxyz'  # Check only lowercase letters
        idx = 10**5  # A large initial index to track the smallest unique index
        
        for i in key:
            x = s.find(i)      # First occurrence of character
            y = s.rfind(i)     # Last occurrence of character
            
            if x != -1 and x == y:  # Only one occurrence
                idx = min(idx, x)   # Track the smallest such index
        
        return idx if idx != 10**5 else -1  # Return result or -1 if none found

What's happening?
•	We're only checking lowercase a-z (assuming s is lowercase).
•	s.find(i) returns the first index of i, or -1 if not found.
•	s.rfind(i) returns the last index of i, or -1 if not found.
•	If both are equal and not -1, it means the character occurs only once.
•	Among all such characters, we track the minimum index.

Detailed Comparison with the Counter Approach

Feature / Criteria	Counter-based Approach	find / rfind Approach
Time Complexity	O(n) – scan + iterate through string	O(26 * n) = O(n) in practice
Space Complexity	O(1) (but technically uses extra dict of size ≤ 26)	✅ O(1) – no extra data structures
Performance on Large Inputs	Fast, but uses a hash map	✅ Slightly faster in practice – no dictionary
String API Usage	Low-level iteration, efficient	✅ High-level API (find, rfind) with clarity
Code Readability	Very readable and explicit	✅ Shorter and cleverly optimized
Extensibility to Unicode	✅ Yes, supports any character	❌ Only works for lowercase English letters
Best for Interview?	✅ Yes, standard and expected	✅ Impressive if explained well

Which One Should You Use?
•	Use the Counter approach if:
o	You want a universal solution that handles Unicode, uppercase, etc.
o	You want clarity and standard data structure usage.
•	Use the find/rfind approach if:
o	You know input is only lowercase letters.
o	You want speed and minimal space.


Question 03: Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:
 
Here, we have dir as the only directory in the root. dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.
In text form, it looks like this (with ⟶ representing the tab character):
dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext
If we were to write this representation in code, it will look like this:
 "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Note that the '\n' and '\t' are the new-line and tab characters. Every file and directory have a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by '/'s. Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext".
Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.
Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note that the testcases are generated such that the file system is valid and no file or directory name has length 0. 
Example 1:
 
Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
Example 2:
 
Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest absolute path to a file.
Example 3:
Input: input = "a"
Output: 0
Explanation: We do not have any files, just a single directory named "a".
Solutions:
Strategy
1.	Split the input by \n to get each line (file or directory).
2.	For each line:
o	Count the number of \t to determine the depth (level of nesting).
o	Strip the tabs to get the name (file or directory).
o	Keep a dictionary or stack to track the path length at each depth.
3.	If the line is a file, compute its absolute path length and update the maximum.
4.	If it’s a directory, update the path length at its depth.
5.	Finally, return the maximum path length found.
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # depth -> current total length at that depth
        for line in input.split('\n'):
            depth = line.count('\t')  # level of nesting
            name = line.lstrip('\t')  # actual name of file or directory
            # If it's a file, calculate full path length
            if '.' in name:
                full_len = path_len[depth] + len(name)
                max_len = max(max_len, full_len)
            else:
                # If it's a dir, store path length for the next depth
                # +1 for the '/' that will be added when joined
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len

Time and Space Complexity
•	Time Complexity: O(n) — where n is the number of characters in the input string. Each line is visited once.
•	Space Complexity: O(d) — where d is the maximum depth of nesting (number of tabs).

Best Leet Code solutions:

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len

🆚 Comparison
Feature	Your Optimized Code	Brute-force Style
Time Complexity	O(n)	O(n*d) where d is max depth (due to join)
Space Complexity	O(d)	O(d) (due to the stack)
Data Structure	dict to store length by depth	list to store names by depth
File Path Calculation	Numeric length using dictionary	Manual string join() at each file
Code Simplicity	Clean, no string joins	More verbose, extra logic for popping stack
Path Reconstruction	Skipped via direct length tracking	Reconstructed using stack + join()
Performance in Deep Trees	Consistently fast	Slower due to repeated string joins
Best For	Performance-critical, interview-quality	Learning/practice but not optimal
________________________________________
🔑 Key Insight
•	Your optimized solution is mathematically tracking path lengths — not the actual paths.
•	Brute-force versions often try to rebuild full strings at each file, which is slow and memory-intensive.
•	Avoiding string join() at every step is a huge win for speed.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
