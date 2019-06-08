from itertools import permutations


def is_palindrome(word):
	if len(word) == 0:
		return False
	if len(word) == 1:
		return True
	for i in range((len(word) // 2) + 1):
		if word[i] != word[-(i + 1)]:
			return False
	return True


def letter_value(letter):
	if len(letter) != 1:
		print("Parameter passed is not a single letter!")
		return None
	if 'A' <= letter.upper() <= 'Z':
		return ord(letter.upper()) - ord('A') + 1
	else:
		print("Parameter passed is not an alphabetical letter!")
		return None


def word_value(word):
	value = 0
	for letter in word:
		value += letter_value(letter)
	return value


def all_permutations(word):
	if type(word) != str:
		str(word)
	perm_list = list(permutations(word))
	res_list = []
	for perm in perm_list: 
		res_list.append(''.join(perm))
	return res_list 