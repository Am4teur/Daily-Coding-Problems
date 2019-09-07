# Daily-Coding-Problems
Python 3 coding solutions to the daily coding problems from https://dailyinterviewpro.com

---

#### Daily Problem 001

Asked by Facebook:
You are given a list of numbers, and a target number k. Return whether or not
there are two numbers in the list that add up to k.

Example:
Given `[4, 7, 1 , -3, 2]` and `k = 5`,
return `True` since `4 + 1 = 5`.

[starting code]
```
def two_sum(list, k):
    # Fill this in.

print two_sum([4,7,1,-3,2], 5)
# True
```

Bonus: Try to do it in a single pass of the list.

[Solution](code-solutions/Solution_001.py)

---

#### Daily Problem 002

Asked by Microsoft:

Given a string, find the length of the longest substring without repeating characters.

```
class Solution:
    def lengthOfLongestSubstring(self, s):
        # Fill this in.

print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxxabcdefghijk"))
# 12
print(Solution().lengthOfLongestSubstring("abcdcabef"))
# 6
```

Can you find a solution in linear time?

[Solution](code-solutions/Solution_002.py)