# from inspect import *
from des import *
import os
import sys

#output_pairs => dictionary index=> {[0,1,1,1],[1,1,1,1]}
def divide_input_and_output():
	if os.path.isfile('inputxor.txt') and os.path.isfile('outputxor.txt'):
		f_inp = open('inputxor.txt','r')
		f_out = open('outputxor.txt','r')
		f_r5 = open('expandr5.txt','r')
		inputxor_list = []
		outputxor_list = []
		for line_inp, line_out, line_r5 in zip(f_inp,f_out, f_r5):
			j = 0
			inputxor_list = [ line_inp[i:i+6] for i in range(0,len(line_inp)-1,6)]
			outputxor_list = [ line_out[j:j+4] for j in range(0,len(line_out)-1,4)]
			r5 = line_r5[:48]
			sbox = 1
			for input_xor,output_xor in zip(inputxor_list,outputxor_list):
				print(sbox)
				print("\n")
				output_pairs = output_possibilities(output_xor)
				input_pairs = input_xor_possibilities(input_xor, output_pairs, sbox)
				# find_key_possibilities(input_pairs, r5, sbox)
				sbox+=1

	else:
		print("No input file found here\n")
		raise SystemExit

def find_key_possibilities(input_pairs, r5, sbox): 
	f_key = open('keyset'+str(sbox)+'.txt','a+')
	key_set = []
	pass



def output_possibilities(output_xor):  
	output_pairs = {}  # {[0,0,0,0]:[0,0,0,0] , [1,0,0,1]: [1,0,1,0]}
	for i in range(0,16):
		input_ = [int(x) for x in '{:04b}'.format(i)];
		input1 = [ str(i) for i in input_]
		input2 =  xor(input1, output_xor);
		output_pairs[convBitList2Int(input2)] = [input1,input2]
	return output_pairs

def get_sbox(sbox):
	if sbox == 1:
		return s1[:]
	elif sbox ==2:
		return s2[:]
	elif sbox == 3:
		return s3[:]
	elif sbox == 4:
		return s4[:]
	elif sbox == 5:
		return s5[:]
	elif sbox == 6:
		return s6[:]
	elif sbox == 7:
		return s7[:]
	elif sbox == 8:
		return s8[:]
	else:
		print("SBOX ERROR\n")
		raise SystemExit

def input_xor_possibilities(input_xor, output_pairs, sbox):
	input_pairs = [];
	for i in range(0, 16):
		output1 = convBitList2Int(output_pairs[i][0]);
		output2 = convBitList2Int(output_pairs[i][1]);
		for rowIndex in range(0,4):
			s1 = get_sbox(sbox)
			for i,val in enumerate(s1[rowIndex]):
				if(val == output1):
					rowIndexB = "{:02b}".format(rowIndex);
					valB = "{:04b}".format(i);
					sixBitInput1 = rowIndexB[0] + valB + rowIndexB[1];
					sixBitInput1 = [int(i) for i in sixBitInput1];
					sixBitInput1 = [str(i) for i in sixBitInput1]
					sixBitInput2 = xor(sixBitInput1, input_xor)
					input_pairs.append([sixBitInput1, sixBitInput2])
					# input_pairs.append([convBitList2Int(sixBitInput1),convBitList2Int(sixBitInput2)]);
	return input_pairs;



divide_input_and_output()
