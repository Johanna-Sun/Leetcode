
# intuition
# chose each one/two point(s) as the midpoint and expand as two sides


class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        result = ""

        if n == 0 or n == 1:
            return  s

        def expand(i,j) -> str:
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        # midpoint is one letter
        for i in range(n):
            current = expand(i,i)
            if len(current) > len(result):
                result = current

        # midpoint is two letters
        for i in range(n-1):
            current = expand(i,i+1)
            if len(current) > len(result):
                result = current

        return result

if __name__ == '__main__':
    print(Solution().longestPalindrome("cbbd"))