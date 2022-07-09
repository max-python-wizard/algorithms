def solution(N):

	if N > 0:
		string_N = str(N)
		current_5 = -1
		next_5 = -1

		while (True):
			current_5 = string_N.find('5', next_5+1)

			if string_N[current_5 + 1] > 5:
				num_without_5 = string_N[:current_5] + string_N[current_5 + 1:]
				return int(num_without_5)

			first_5 = string_N.find('5', first_5+1)

			elif string_N[first_5 + 1] < 5:
				num_without_5 = string_N[:first_5] + string_N[first_5 + 1:]
				return int(num_without_5)
		print(first_5)

		num_without_5 = string_N[:first_5] + string_N[first_5+1:]
		return num_without_5


A = 15958
B = -5859
C = -5000

print(solution(A))
print(solution(B))
print(solution(C))
