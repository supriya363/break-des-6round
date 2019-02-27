from des import *
import itertools
import sys
import os
# l5_XOR = "04000000"

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
				# print("Bit String representation of cipher 1: {0}\n".format(c1))
				# print("Bit String representation of cipher 2: {0}\n".format(c2))
				c1_rev = ''.join(initial_permutation(list(c1)))  
				c2_rev = ''.join(initial_permutation(list(c2)))
				# print("Reverse Permutation of cipher 1: {0}\n".format(c1_rev))
				# print("Reverse Permutation of cipher 2: {0}\n".format(c2_rev)) 
				f_out.write(c1_rev + ' ' + c2_rev+ '\n') 
			f_in.close()
			f_out.close()
	else:
		print("No input pair file found\n")
		raise SystemExit


#compute xor of ciphertext pairs in bitstring form in finalcipher.txt and place them in
# cipherxor.txt in the form leftxor rightxor
#expand l6 and l6' and place them in expandr5.txt
#compute input to sbox and place it in inputxor.txt
def compute_sbox_xor():
	if os.path.isfile('finalcipher.txt'):
		f_in = open('finalcipher.txt','r')
		f_out = open('cipherxor.txt','w')
		f_exp = open('expandr5.txt','w')
		f_sbox_inp = open('inputxor.txt','w')
		f_sbox_out = open('outputxor.txt','w')
		for line in f_in:
			c1 = line[:64]
			c2 = line[65:-1]
			c1_l6 = c1[:32]
			c1_r6 = c1[32:]
			c2_l6 = c2[:32]
			c2_r6 = c2[32:]

			# print("".format())
			c1_exp = ''.join(expansion(list(c1_l6)))  	#to compute e(r5)
			c2_exp = ''.join(expansion(list(c2_l6)))  	#to comput e(r5')
			l6_xor = ''.join(xor(c1_l6,c2_l6))					
			r6_xor = ''.join(xor(c1_r6,c2_r6))
			# permutation_out = xor(r6_xor),convert_xor_to_input(l5_XOR))
			permutation_out = list(r6_xor)  			#will consider only appropriate 20 bits
			sbox_input_xor = ''.join(xor(c1_exp,c2_exp)) 
			sbox_output_xor = ''.join(inverse_permute(permutation_out))


			f_out.write(l6_xor + ' ' + r6_xor + '\n')
			f_exp.write(c1_exp + ' ' + c2_exp + '\n') #e(r5) and e(r5')
			f_sbox_inp.write(sbox_input_xor + '\n')
			f_sbox_out.write(sbox_output_xor + '\n')

		f_in.close()
		f_out.close()
		f_exp.close()
		f_sbox_inp.close()
		f_sbox_out.close()
	else:
		print("No input file found\n")
		raise SystemExit


reverse_permute()
compute_sbox_xor()
