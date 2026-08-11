class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum=nums[0]
        answer=-1
        for num in nums[1:]:
            if num>minimum:
                difference=num-minimum
                if difference>answer:
                    answer=difference
            if num<minimum:
                minimum=num
        return answer