# Oryginalny kod pythona dla ciągu fibonacciego z rekurencją
def fibonacci_recursive(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# mój kod dynamiczny zapisujący wyniki do listy w trakcie tworzenia ciągu
def fib(n):
	fib_results = [1, 1]
	for i in range(2, n):
		# print(i)
		fib_results.append(fib_results[i - 1] + fib_results[i - 2])
	return fib_results[-1]