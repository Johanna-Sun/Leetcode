
# intuition
# pick a number + 2sum


from collections import defaultdict

class Solution:
    def threeSum(self, nums):

        result = []
        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < len(nums) and k > i and j != k:
                currentSmall = nums[j]
                currentLarge = nums[k]
                if currentSmall + currentLarge == target and sorted([nums[i],currentSmall,currentLarge]) not in result:
                    result.append(sorted([nums[i],currentSmall,currentLarge]))
                    j += 1
                    k -= 1
                else:
                    if (currentSmall + currentLarge) > target:
                        k -= 1
                    else:
                        j += 1


        return result


if __name__ == '__main__':
    print(Solution().threeSum([0,0,0]))