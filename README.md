# Affine Ciphers

Affine ciphers use an affine transformation (e.g. `f(x) = a * x + b mod 26` ) to encrypt a plaintext character by character.

The simplest affine cipher uses the following functions:

`E(p) = a * p + b`

where the pair `(a, b)` constitutes the key. The decryption function is:

`D(c) = a^-1 * c + a^-1 * b`

Since the decryption is doable only if there exists a mulitplicative inverse of `a` in `Z26` (the congruence set) the condition `GCD(a, 26) = 1` must hold. Because of this reason the space of the keys is very limited. In fact `a` can assume exactly 12 different values (i.e. all coprimes with 26) while `b` can assume 26 values. Hence the total space is made of 12 * 26 = __312__ possible keys. Easily breakable by bruteforce.

# Affine Ciphers breaker

This breaker uses a dictionary to check if the plaintext found by applying a bruteforce attack "makes sense" (i.e. contains at least a minimum number of English words). This is why a single round of attack may take a few minutes (there is no optimization of any kind, pull requests are welcome!). The default sensibility is 5. This value (the last parameter to the script) indicates the minimum number of English words that the decrypted plaintext must contain.

## Usage

From a terminal run:

`python affine_cipher.py path_to_ciphertext path_to_dictionary [sensibility]`

The dictionary must be a text file containing a word per line. One is included in the repository. The list of probable plaintexts is output on the standard output.
