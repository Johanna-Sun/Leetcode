
# intuition
# start from the lowest position
# we want to shift the highest point of the "mountain" to left a bit

# 1 2 8 7 9 3 2


class Solution:
    def nextPermutation(self, nums):
        peek = -1
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if nums[i] < nums[i+1]:
                peek = i
                break

        if peek is -1:
            nums.reverse()
        else:
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] > nums[peek]:
                    # flag = i
                    current = nums[peek]
                    nums[peek] = nums[i]
                    nums[i] = current
                    break
            nums[peek+1 : len(nums)] = reversed(nums[peek + 1 : len(nums)])
        return nums

if __name__ == '__main__':
    print(Solution().nextPermutation([1,2,3]))
