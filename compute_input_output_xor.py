from des import *
import itertools
import sys
import os


#take ciphertext pairs from cipher.txt and apply reverse permuation on them
#place the resulting pair in finalcipher.txt
def reverse_permute():
	# if os.path.isfile('cipher.txt'):
	if os.path.isfile('cipher.txt'):
			f_in = open('cipher.txt','r')
			f_out = open('finalcipher.txt','w')
			for line in f_in:
				# diff = get_diff_of_cipherpair(line_out[:64],line_out[65:-1])[:32]
				c1 = line[:64]
				c2 = line[65:-1]
				c1_rev = ''.join(initial_permutation(list(c1)))  
				c2_rev = ''.join(initial_permutation(list(c2))) 
				f_out.write(c1_rev + ' ' + c2_rev+ '\n') 
			f_in.close()
			f_out.close()
	else:
		print("No input pair file found\n")
		raise SystemExit


#compute xor of ciphertext pairs in bitstring form in finalcipher.txt and place them in
# cipherxor.txt in the form leftxor rightxor
def compute_xor_of_cipherpair():
	if os.path.isfile('finalcipher.txt'):
		f_in = open('finalcipher.txt','r')
		f_out = open('cipherxor.txt','w')
		for line in f_in:
			c1 = line[:64]
			c2 = line[65:-1]
			c1_l6 = c1[:32]
			c1_r6 = c1[32:]
			c2_l6 = c2[:32]
			c2_r6 = c2[32:]
			l6_xor = ''.join(xor(list(c1_l6),list(c2_l6)))
			r6_xor = ''.join(xor(list(c1_r6),list(c2_r6)))
			f_out.write(l6_xor + ' ' + r6_xor + '\n')
		f_in.close()
		f_out.close()
	else:
		print("No input file found\n")
		raise SystemExit


#expand l6 and l6' and place them in expandr5.txt
#compute input to sbox and place it in inputxor.txt
def compute_input_xor_of_sbox():
	pass


# compute output xor of each pair and place them in outputxor.txt
def compute_output_xor_of_sbox():
	pass



reverse_permute()
compute_xor_of_cipherpair()