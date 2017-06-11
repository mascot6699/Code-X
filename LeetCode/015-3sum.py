class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        if len_nums < 3:
            return []
        elif len_nums == 3 and sum(nums) == 0:
            print(nums)
            return [sorted(nums)]
        nums = sorted(nums)
        a, i = [] , 0
        while i < (len_nums-2):
            nums_i = nums[i]
            if (i == 0 or nums_i != nums[i-1]) and nums_i < 1:
                j, k = i+1, len_nums-1
                if nums_i + nums[j] + nums[j+1] > 0:
                    return a
                while j < k:
                    sum_to_be_zero = nums_i + nums[j] + nums[k]
                    if sum_to_be_zero < 0:
                        j += 1
                    elif sum_to_be_zero > 0:
                        k -= 1
                    else:
                        a.append([nums_i, nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return a
        
if __name__ == '__main__':
    a = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print a