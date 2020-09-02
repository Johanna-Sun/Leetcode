## Intuition:
## decide which side the target is in and devide and conquer


class Solution:
    def search(self, nums, target):
        if len(nums) <= 0:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] is target:
                return mid

            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid+1] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid

        if nums[left] is target:
            return left
        else:
            return -1




if __name__ == '__main__':
    print(Solution.search([4,5,6,7,0,1,2],0))