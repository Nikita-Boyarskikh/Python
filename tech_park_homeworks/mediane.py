def mediane(*nums):
	if len(nums) == 0:
		print("NaN");
	elif len(nums)%2==0:
		print((nums[len(nums)//2-1]+nums[len(nums)//2])/2);
	else:
		print(nums[len(nums)//2]);

mediane(1,2,3,5,6,7);
