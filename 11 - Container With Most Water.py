
# intuition
# The only situation that the area might get bigger is by moving the short side as the short side is the determining factor

class Solution:
    def maxArea(self, height) -> int:

        left = 0
        right = len(height) - 1
        result = min(height[left],height[right])*(right-left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            currentArea = min(height[left],height[right])*(right-left)
            if result < currentArea:
                result = currentArea;

        return result




if __name__ == '__main__':
    print(Solution().maxArea([1,1]))