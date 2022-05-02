# https://leetcode.com/submissions/detail/691809539/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r = n - 1

        for i in range(n):
            if nums[i] % 2 == 1:
                for j in reversed(range(i + 1, r + 1)):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        r = j
                        break
                else:
                    break

        return nums
