from math import floor, sqrt
from my_modules.digits import get_rotations


def sieve_of_eratosthenes(limit):
	are_primes = [True for _ in range(limit + 1)]
	are_primes[0:1] = [False, False]
	for i in range(2, floor(sqrt(limit + 1)) + 1):
		if are_primes[i]:
			for j in range(i * i, limit + 1, i):
				are_primes[j] = False
	primes = []
	for i in range(2, limit + 1):
		if are_primes[i]:
			primes.append(i)
	return primes
 	

def is_prime(n):
	if n <= 1: 
		return False
	if n <= 3: 
		return True
	if n % 2 == 0 or n % 3 == 0: 
		return False  
	i = 5
	while i * i <= n: 
		if n % i == 0 or n % (i + 2) == 0: 
			return False
		i += 6  
	return True


def is_circular_prime(n):
	rotations = get_rotations(n)
	for p in rotations:
		if not is_prime(p):
			return False
	return True


def is_lr_prime(n):
	for i in range(len(str(n))):
		if not is_prime(int(str(n)[i:])):
			return False
	return True


def is_rl_prime(n):
	for i in range(len(str(n)) - 1, -1, -1):
		if not is_prime(int(str(n)[:i + 1:])):
			return False
	return True


def prime_factorization(n, primes = []):
	if n < 2:
		return None
	if is_prime(n):
		return {n : 1}
	if primes == []:
		primes = sieve_of_eratosthenes(n // 2)
	factorization = {}
	for prime in primes:
		while (n > 1) and (n % prime == 0):
			if prime not in factorization:
				factorization[prime] = 1
			else:
				factorization[prime] += 1
			n //= prime
		if n == 1:
			break
	return factorization