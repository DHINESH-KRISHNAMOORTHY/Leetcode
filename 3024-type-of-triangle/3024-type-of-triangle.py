class Solution(object):
    def triangleType(self, nums):
            if(nums[0] + nums[1] <= nums[2] or
               nums[1] + nums[2] <= nums[0] or
               nums[0] + nums[2] <= nums[1]):
               return "none"
            else:

                a=len(set(nums))
                if a==1:
                    return "equilateral"
                elif a==2:
                    return "isosceles"
                else:
                    return "scalene"