from des import *
from xorpairs import *

def output_possibilities(output_xor):
	#returns a list of output pairs possible
	pass


def input_xor_possibilities(input_xor, output_pairs):
	#returns list of input pairs possible
	pass

def find_key_possibilities(input_pairs):
	pass

def inspect_possibilities(input_xor, output_xor):
	output_pairs = output_possibilities(output_xor)
	input_pairs = input_possibilities(input_xor, output_pairs)
	key_set = find_key_possibilities(input_pairs)
	pass

def start_inspecting(r6, r5, l5):
	#xor l5 and r6 to get permutation output
	#inverse permutation to get substitution output xor
	#take expansion of r5 which is inputxor to sbox
	input_xor = [] #bit arrays
	output_xor = [] #bit arrays
	inspect_possibilities(input_xor, output_xor)
	pass
