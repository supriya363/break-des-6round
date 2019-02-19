from des import *
from xorpairs import *
from generate_textstrings import *

start_bit = 0
end_bit = 6


def output_possibilities(output_xor):  
	output_pairs = {}  # {[0,0,0,0]:[0,0,0,0] , [1,0,0,1]: [1,0,1,0]}
    for i in range(0,16):
        input1 = [int(x) for x in '{:04b}'.format(i)];
        input2 =  xor(input1, output_xor);
        output_pairs[convBitList2Int(input2)] = [input1,input2]
    return output_pairs;

#inputXor => 6bit number
#output_pairs => dictionary index=> [[0,1,1,1],[1,1,1,1]]
def input_xor_possibilities(input_xor, output_pairs):
	input_pairs = [];
    for i in range(0, 16):
        output1 = convBitList2Int(output_pairs[i][0]);
        output2 = convBitList2Int(output_pairs[i][1]);
        for rowIndex in range(0,4):
            for i,val in enumerate(s1[rowIndex]):
                if(val == output1):
                    rowIndexB = "{:02b}".format(rowIndex);
                    valB = "{:04b}".format(i);
                    sixBitInput1 = rowIndexB[0] + valB + rowIndexB[1];
                    sixBitInput1 = [int(i) for i in sixBitInput1];
                    sixBitInput2 = xor(sixBitInput1, input_xor)
                    input_pairs.append([convBitList2Int(sixBitInput1),convBitList2Int(sixBitInput2)]);
    return input_pairs;

def find_key_possibilities(input_pairs, r5): 
	key_set = []
	for u1 in input_pairs.keys():
		key_set.append(xor(u1, r5[start_bit:end_bit]))
	return key_set

def inspect_possibilities(input_xor, output_xor, r5):  #all are bit arrays

	output_pairs = output_possibilities(output_xor)
	input_pairs = input_possibilities(input_xor, output_pairs)
	key_set = find_key_possibilities(input_pairs, r5) 
	pass

def start_inspecting(r6xor, r5xor, l5xor, r5): 
	permutation_output = xor(l5xor, r6xor)
	output_xor = inverse_permute(permutation_output) 
	input_xor = expansion(r5xor)
	actual_input = expansion(r5)
	inspect_possibilities(input_xor, output_xor, actual_input)
    


