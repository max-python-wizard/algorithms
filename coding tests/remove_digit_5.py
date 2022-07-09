# Question: Write a function solution that, given an integer N, returns the maximum possible value obtainable by deleting
# one ‘5’ digit from the decimal representation of N. It is guaranteed that N will contain at least one “5′ digit.

def rem_5(n):
	str_n = str(n)

	last_5 = -1
	locations_5 = []

	while (True):
		loc_5 = str_n.find('5', last_5 + 1)

		if loc_5 == -1:
			break

		locations_5.append(loc_5)
		last_5 = loc_5

	nums_wout_5 = []
	for l in locations_5:
		n_wout_5 = str_n[:l] + str_n[l+1:]
		# print(n_wout_5)
		nums_wout_5.append(n_wout_5)

	nums = []
	for l in nums_wout_5:
		nums.append(int(l))

	return max(nums)


print(rem_5(15958), " should be 1958")
print(rem_5(-5859), " should be -589")
print(rem_5(-5000), " should be 0")
