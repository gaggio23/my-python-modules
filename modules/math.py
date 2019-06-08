import math

# Decimal to any other base
def base_conversion(num, base):
    conv_str = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num < base:
        return conv_str[num]
    else:
        return base_conversion(num // base, base) + conv_str[num % base]


def is_pythagorian_triple(*triple):
	if len(triple) != 3:
		print("Passed tuple has not 3 elements!")
		return None
	if (type(triple[0]) != int) or (type(triple[1]) != int) or (type(triple[2]) != int):
		print("One or more of passed arguments is not of type 'int'!")
		return None
	if ((triple[0] ** 2) + (triple[1] ** 2)) == (triple[2] ** 2):
		return True
	else:
		return False


def get_pythagorian_triples(sides_sum):
	pythagorian_triples = []
	for n in range(1, sides_sum):
		for m in range(n + 1, sides_sum):
			if (((m + n) % 2) != 0) and (math.gcd(m, n) == 1):
				for k in range(1, sides_sum):
					a = k * (m ** 2 - n ** 2)
					b = k * (2 * m * n)
					c = k * (m ** 2 + n ** 2)
					if (a + b + c) == sides_sum:
						pythagorian_triples.append((a, b, c))
					elif (a + b + c) > sides_sum:
						break
	return pythagorian_triples


def champernowne_constant(length):
	constant = "0."
	i = 1
	while len(constant) <= length:
		constant += str(i)
		i += 1
	return constant


def digital_root(n):
	return ((n - 1) % 9) + 1


def is_square(n):
	if (n == 0) or (n == 1):
		return True
	if n < 0:
		return False

	if digital_root(n) not in (1, 4, 7, 9):
		return False
	if base_conversion(n, 16)[-1] not in ('0', '1', '4', '9'):
		return False
	if len(str(n)) > 1:
		last_digit = int(str(n)[-1])
		second_last_digit = int(str(n)[-2])
		if (last_digit == 5) and (second_last_digit != 2):
			return False
		if (last_digit == 6) and ((second_last_digit % 2) == 0):
			return False
		if (last_digit in (1, 4, 9)) and ((second_last_digit % 2) != 0):
			return False
	if (int(math.sqrt(n)) ** 2) == n:
		return True
	else:
		return False


def is_triangle_number(n):
	return is_square(8 * n + 1)


def nth_triangle_number(n):
	return n * (n + 1) // 2


def nth_triangle_numbers(n):
	triangle_numbers = []
	for i in range(1, n + 1):
		triangle_numbers.append(nth_triangle_number(i))
	return triangle_numbers


def is_pentagonal_number(n):
	k = (math.sqrt(24 * n + 1) + 1) / 6
	if k - int(k) == 0:
		return True
	else:
		return False


def nth_pentagonal_number(n):
	return n * (3 * n - 1) // 2


def nth_pentagonal_numbers(n):
	pentagonal_numbers = []
	for i in range(1, n + 1):
		pentagonal_numbers.append(nth_pentagonal_number(i))
	return pentagonal_numbers


def is_hexagonal_number(n):
	k = (math.sqrt(8 * n + 1) + 1) / 4
	if k - int(k) == 0:
		return True
	else:
		return False


def nth_hexagonal_number(n):
	return n * (2 * n - 1)


def nth_hexagonal_numbers(n):
	hexagonal_numbers = []
	for i in range(1, n + 1):
		hexagonal_numbers.append(nth_hexagonal_number(i))
	return hexagonal_numbers