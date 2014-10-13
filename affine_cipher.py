"""
Affine ciphers use an affine function of the type f(x) = ax + b % 26 with the coefficient a and b forming the key.
A requirement for such ciphers is that the GCD(a, 26) = 1.
Since the only values for which GCD(a, 26) = 1 are (1 3 5 7 9 11 15 17 19 21 23 25) (i.e. 12 values) the total space of the keys is 12 * 26 = 312.
A brute-force attack takes very little on a modern computer.
"""

import sys

def main(args):
	if len(args) != 3:
		print_usage(args)
		exit()

	mul_inverses = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
	cipher_text_file = args[1]
	cipher_text = "".join(open(cipher_text_file, "r").readlines())
	dictionary_file = args[2]
	dictionary = open(dictionary_file, "r").readlines()
	cur_text = ""
	keys_tried = 0
	for a in mul_inverses:
		keys_tried += 1
		for b in xrange(1, 26):
			keys_tried += 1
			for x in xrange(0, len(cipher_text)):
				cur_text += transform(a, b, cipher_text[x], True)
			if makes_sense(cur_text, dictionary, 5):
				print "Probable plaintext: " + cur_text
			cur_text = ""

def map_char(c, encoding):
	if encoding == "alpha":
		return c - 97
	if encoding == "ascii":
		return c + 97
	else:
		raise Exception("Choose a mapping mode (alpha or ascii)")

def makes_sense(text, dictionary, n):
	"""
	Check if the text contains at least n words from the given dictionary.
	"""
	count = 0
	for w in dictionary:
		try:
			text.index(w.strip())
			count += 1
			if count >= n:
				return True
		except Exception:
			pass
	return False


def transform(a, b, x, decrypt = False):
	"""
	Encrypt or decrypt the character x using the coefficients a and b
	"""
	if decrypt:
		denom = get_mul_inverse(a, 26)
		x_index = map_char(ord(x), "alpha")
		decrypted_alpha = (denom * x_index - denom * b) % 26
		decrypted_ascii = chr(map_char(decrypted_alpha, "ascii"))
		# print "Decrypted %s with keys %d, %d resulting in %s" % (x, a, b, decrypted_ascii)
		return decrypted_ascii
	else:
		return (a * x + b) % 26

def print_usage(args):
	print "Usage: " + args[0] + " path_to_ciphertext path_to_dictionary"

def get_mul_inverse(n, mod):
	for i in xrange(1, mod):
		if (n * i) % mod == 1:
			return i
	else:
		raise Exception("Could not find multiplicative inverse for " + str(n) + " in Z " + str(mod))




main(sys.argv)
# print get_mul_inverse(9, 26)