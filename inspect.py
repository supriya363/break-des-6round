from des import *
from xorpairs import *
from generate_textstrings import *

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

def start_inspecting(r6, r5, l5): #DONE
	permutation_output = xor(l5, r6)
	output_xor = inverse_permute(permutation_output) #DONE
	input_xor = expansion(r5)
	inspect_possibilities(input_xor, output_xor)

