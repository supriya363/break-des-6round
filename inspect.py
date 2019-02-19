from des import *
from xorpairs import *
from generate_textstrings.py import *

def output_possibilities(output_xor):   #SUP
	#returns a list of output pairs possible
	pass


def input_xor_possibilities(input_xor, output_pairs):  #ARUN
	#returns list of input pairs possible
	pass

def find_key_possibilities(input_pairs): #SUP
	pass

def inspect_possibilities(input_xor, output_xor):
	output_pairs = output_possibilities(output_xor)
	input_pairs = input_possibilities(input_xor, output_pairs)
	key_set = find_key_possibilities(input_pairs) #r5 to be passed
	pass

def start_inspecting(r6, r5, l5): #SUP
	#xor l5 and r6 to get permutation output
	#inverse permutation to get substitution output xor
	#take expansion of r5 which is inputxor to sbox
	input_xor = [] #bit arrays
	output_xor = [] #bit arrays
	inspect_possibilities(input_xor, output_xor)
	pass
