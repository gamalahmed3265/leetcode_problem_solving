nums = [-1,0,3,5,9,12];target=9

class Solution:
	def search(self,nums: list[int], target):
		
		left=0
		right=len(nums)-1
		
		while left<=right:
			medium=(left+right)//2
			if target==nums[medium]:
				return medium
			if target> nums[medium]:
				left=medium+1
			else:
				right=medium-1
		else:
			return -1

sol=Solution()


print(sol.search(nums,target))