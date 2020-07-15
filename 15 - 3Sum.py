
# intuition
# pick a number + 2sum


from collections import defaultdict

class Solution:
    def threeSum(self, nums):

        result = []
        nums.sort()

        for i in range(len(nums)):

            # if we already dealt with current target then continue
            if i > 0 and nums[i-1] == nums[i]:
                i += 1
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                currentSmall = nums[j]
                currentLarge = nums[k]
                if currentSmall + currentLarge == target:
                    result.append([nums[i],currentSmall,currentLarge])
                    j += 1
                    # no need to deal with k cuz the set is different if any one amont it is different
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                else:
                    if (currentSmall + currentLarge) > target:
                        k -= 1
                    else:
                        j += 1


        return result


if __name__ == '__main__':
    print(Solution().threeSum([1,0,0]))