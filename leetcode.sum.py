
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        positionHash = {}
        result       = []
        for i in range(len(nums)):
            partner  = target - nums[i]
            if nums[i] not in positionHash:
                positionHash[nums[i]] = [i]         # save the position for this value
            else:
                positionHash[nums[i]].append(i)     # add another position to this value
            # lets check if the partner value is already there
            if partner in positionHash:
                # yes, so now we now
                print(partner)
                result.append(positionHash[partner] + [i])
        print(positionHash)
        return result

    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        return strx == strx[::-1]

        
nums = [2,7,2,11,15, -6]
target = 9
# print(Solution().twoSum(nums,target))
print(Solution().isPalindrome(11011))