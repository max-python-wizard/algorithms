def ret_dec(table):
	sum_ = 0
	number_bits = len(table)
	# print(number_bits)

	for i in range(number_bits):
		power = number_bits - i - 1
		if table[i] == 1:
			sum_ += pow(2, power)

	return sum_


def converter_ac(input_v, extreme_lower=-10, extreme_upper=10, resolution_bits=8):

	if input_v > extreme_upper or input_v < extreme_lower:
		print("Input voltage can't be below or above lower and upper extreme.")

	full_scale_voltage_range = extreme_upper - extreme_lower
	# print(full_scale_voltage_range)
	input_v_from_lower_extreme = input_v + (0 - extreme_lower)

	voltage_intervals = pow(2, resolution_bits)
	range_v = full_scale_voltage_range / voltage_intervals
	# print(range_v)
	table = [0] * resolution_bits

	for i in range(len(table)):
		table[i] = 1
		# print(table)
		dec = ret_dec(table)
		voltage_step = dec * range_v
		# print(voltage_step)
		if voltage_step > input_v_from_lower_extreme:
			table[i] = 0

	return table

extreme_lower = float(input("What's the bottom border of range?"))
extreme_upper = float(input("What's the bottom border of range?"))

print(converter_ac(7.35, extreme_lower, extreme_upper))
