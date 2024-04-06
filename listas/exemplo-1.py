nums = [17, 33, 23, 11, 8, 15, 9]
for i in range(len(nums) -1):
	if nums[i] > nums [i+1]:
		aux = nums[1]
		nums[i] = nums[i+1]
		nums[i+1] = aux