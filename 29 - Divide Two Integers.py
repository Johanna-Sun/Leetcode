

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # edge cases
        # wont deal with divisor = 0 cuz the question says it wont
        # divisor = 1
        if divisor == 1:
            return max(pow(-2,31),min(pow(2,31)-1,dividend))
        else:
            if divisor == -1:
                return max(pow(-2,31),min(pow(2,31)-1,-dividend))

        # sign
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0

        while divisor <= dividend:
            _divisor = divisor
            count = 1
            while _divisor <= dividend:
                dividend -= _divisor
                _divisor = _divisor * 2
                result += count
                count = count * 2

        return max(pow(-2,31),min(pow(2,31)-1,result)) if sign else max(pow(-2,31),min(pow(2,31)-1,-result))


if __name__ == '__main__':
    print(Solution().divide(-2147483648,-1))