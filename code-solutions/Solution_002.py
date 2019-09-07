class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        count = 0
        max = 0
        i = 0
        while(i < len(s)):
            if(s[i] in seen):
                if(count > max):
                    max = count
                i = seen[s[i]] + 1
                seen = {}
                seen[s[i]] = i
                count = 1
            else:
                seen[s[i]] = i
                count += 1
            i += 1

        if(count > max):
            max = count
        return max
      

print(Solution().lengthOfLongestSubstring("abrkaabcdefghijjxxxabcdefghijk"))
# 12
print(Solution().lengthOfLongestSubstring("abcdcabef"))
# 6