from des import *
from xorpairs import *
from generate_textstrings import *

start_bit = 0
end_bit = 6


def output_possibilities(output_xor):  
	output_pairs = {}  # {[0,0,0,0]:[0,0,0,0] , [1,0,0,1]: [1,0,1,0]}


	pass


def input_xor_possibilities(input_xor, output_pairs):
	#returns list of input pairs possible
	input_pairs = {}
	pass

def find_key_possibilities(input_pairs, r5): #SUP
	key_set = []
	for u1 in input_pairs.keys():
		key_set.append(xor(u1, r5[start_bit:end_bit]))
	return key_set

def inspect_possibilities(input_xor, output_xor, r5):  #all are bit arrays

	output_pairs = output_possibilities(output_xor)
	input_pairs = input_possibilities(input_xor, output_pairs)
	key_set = find_key_possibilities(input_pairs, r5) #r5 to be passed
	pass

def start_inspecting(r6xor, r5xor, l5xor, r5): #DONE
	permutation_output = xor(l5xor, r6xor)
	output_xor = inverse_permute(permutation_output) #DONE
	input_xor = expansion(r5xor)
	actual_input = expansion(r5)
	inspect_possibilities(input_xor, output_xor, actual_input)

