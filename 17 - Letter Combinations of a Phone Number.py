
# intuition
# pass on current combo (thus recursive method)

class Solution:
    def letterCombinations(self, digits: str):

        if len(digits) == 0:
            return []

        phone = { "1": "",
                  "2": "abc",
                  "3": "def",
                  "4": "ghi",
                  "5": "jkl",
                  "6": "mno",
                  "7": "pqrs",
                  "8": "tuv",
                  "9": "wxyz"}
        result = []


        def push(currentIndex,currentStr):

            if (currentIndex == len(digits)):
                result.append((currentStr))
                return

            for i in phone[digits[currentIndex]]:
                push(currentIndex + 1, currentStr + i)


        push(0,"")

        return result


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
