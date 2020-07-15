
# intuition
# they automatically match as long as there's always a right paren at the right side of left paren

class Solution:
    def generateParenthesis(self, n: int):

        result = []

        def push(l,r,str):
            if n == 0:
                return
            if l == n and r == n:
                result.append(str)
                return
            if l < r:
                return
            if l < n:
                push(l+1,r,str+"(")
            if r < l:
                push(l,r+1,str+")")

        push(0,0,"")
        return result

if __name__ == '__main__':
    print(Solution().generateParenthesis(3))