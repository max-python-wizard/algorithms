# Question: Write a function solution that, given an integer N, returns the maximum possible value obtainable by deleting
# one ‘5’ digit from the decimal representation of N. It is guaranteed that N will contain at least one “5′ digit.

def remove_5(n):
	str_n = str(n)
	start_search = -1
	locations_5 = []

	while (True):
		loc_5 = str_n.find('5', start_search + 1)
		if loc_5 != -1:
			locations_5.append(loc_5)
			start_search = loc_5

		else:
			break

	nums_wout_5 = []
	for l in locations_5:
		without_5 = str_n[:l] + str_n[l+1:]
		nums_wout_5.append(int(without_5))

	return max(nums_wout_5)

print(remove_5(12345))
print(remove_5(1452345))
print(remove_5(1452345))


print(remove_5(15958), " should be 1958")
print(remove_5(-5859), " should be -589")
print(remove_5(-5000), " should be 0")