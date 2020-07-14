
# intuition:
# have a window to expand its right side and to move its left side if sth repeats
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        window = defaultdict(int)
        for i in range(len(s)):
            window[s[i]] += 1
            while window.get(s[i]) == 2 :     # if sth repeats
                window[s[left]] = window.get(s[left],0) - 1  #move its left side to right
                left += 1
            maxLength = max(maxLength, i - left + 1)
        return maxLength


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))