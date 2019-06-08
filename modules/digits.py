from math import factorial


def digits_number(x):
	return len(str(abs(x)))


def has_digit(x, digit):
	if digits_number(digit) != 1:
		print("Second parameter not a digit")
		return False
	if str(digit) in str(x):
		return True
	else:
		return False


def join_numbers(*args):
	res = ""
	for arg in args:
		res += str(arg)
	return int(res)


def number_to_list(n):
	num_list = []
	for d in str(abs(n)):
		num_list.append(int(d))
	return num_list


def get_rotations(n):
	rotations = []
	for i in range(digits_number(n)):
		rotations.append(int(str(n)[i:] + str(n)[:i]))
	return rotations


def sum_digit_factorial(n):
	res = 0
	for d in number_to_list(n):
		res += factorial(d)
	return res


def has_different_digits(n):
	found_digits = []
	while n > 0:
		digit = n % 10
		if digit in found_digits:
			return False
		else:
			found_digits.append(digit)
			n //= 10
	return True


def missing_digit(large, small):
	if large <= small:
		print("First argument needs to be the largest one")
		return None
	if digits_number(large) - digits_number(small) != 1:
		print("Numbers do not differ for one digit")
		return None
	large_list = list(str(large))
	small_list = list(str(small))
	for n in small_list:
		if n not in large_list:
			#print("small number digits not contained in largest one's")
			return None
		else:
			large_list.remove(n)
	return int(large_list.pop())


def is_number_pandigital(n):
	if '0' not in str(n) and digits_number(n) <= 9 and has_different_digits(n):
		for i in range(1, digits_number(n) + 1):
			if str(i) not in str(n):
				return False
		return True
	else:
		return False