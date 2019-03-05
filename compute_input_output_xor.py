from des import *
import itertools
import sys
import os


def reverse_permute():
	if os.path.isfile('cipher.txt'):
			f_in = open('cipher.txt','r')
			f_out = open('finalcipher.txt','w')
			for line in f_in:
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


			c1_exp = ''.join(expansion(list(c1_r6)))  	#to compute e(r5)
			c2_exp = ''.join(expansion(list(c2_r6)))  	#to comput e(r5')
			l6_xor = ''.join(xor(c1_l6,c2_l6))					
			r6_xor = ''.join(xor(c1_r6,c2_r6))
			permutation_out = list(l6_xor)  			#will consider only appropriate 20 bits
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
