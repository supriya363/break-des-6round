# from inspect import *
from des import *
import os
import sys

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
    input_xor_val = ''.join(input_xor);
    for i in range(0, 16):
        output1 = convBitList2Int(output_pairs[i][0]);
        output2 = convBitList2Int(output_pairs[i][1]);
        u1_possibility = [];
        u2_possibility = [];
        for rowIndex in range(0,4):
            s1 = get_sbox(sbox)
            for i,val in enumerate(s1[rowIndex]):
                if(val == output1):
                    rowIndexB = "{:02b}".format(rowIndex);
                    valB = "{:04b}".format(i);
                    sixBitInput1 = rowIndexB[0] + valB + rowIndexB[1];
                    #u1_possibility.append(int(sixBitInput1,2));
                    u1_possibility.append(sixBitInput1);
                if(val == output2):
                    rowIndexB = "{:02b}".format(rowIndex);
                    valB = "{:04b}".format(i);
                    sixBitInput2 = rowIndexB[0] + valB + rowIndexB[1];
                    #u2_possibility.append(int(sixBitInput2,2));
                    u2_possibility.append(sixBitInput2);


        for u1 in u1_possibility:
            for u2 in u2_possibility:
                u1u2_xor = xor(u1, u2);
                u1u2_xor = ''.join(u1u2_xor);
                if(input_xor_val == u1u2_xor):
                    u1_str = [str(i) for i in u1];
                    u2_str = [str(i) for i in u2];
                    input_pairs.append([u1_str,u2_str]);
                
    # 					input_pairs.append([sixBitInput1, sixBitInput2])
    # 					input_pairs.append((convBitList2Int(sixBitInput1),convBitList2Int(sixBitInput2)));
    return input_pairs;

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
			# print(inputxor_list)
			# print(outputxor_list)
			r5 = line_r5[:48]
			#print(r5)
			
			sbox = 1
			for input_xor,output_xor in zip(inputxor_list,outputxor_list):
				# print(sbox)
				output_pairs = output_possibilities(output_xor)
				input_pairs = input_xor_possibilities(input_xor, output_pairs, sbox)
				# print(len(input_pairs))
				find_key_possibilities(input_pairs, r5, sbox)
				sbox+=1

	else:
		print("No input file found here\n")
		raise SystemExit

def make_key_list():	# Returns list of all possible 64 keys[6 bits]
	key_list=[]
	for i in range(64):
		tmp=bin(i)[2:]
		while len(tmp) < 6:
			tmp = "0" + tmp
		key_list.append([tmp,0])
	return key_list

def find_key_possibilities(input_pairs, r5, sbox):
	f_key = open('keyset'+str(sbox)+'.txt','w+')
	for i in range(len(input_pairs)):
		key_list[sbox-1][int(''.join(xor(input_pairs[i][0], r5[(sbox-1)*6:(sbox-1)*6+6])),2)][1] += 1	# xor of 6 bits of key and corresponding S-box input
	
	for i in range(64):
		f_key.write(str(key_list[sbox-1][i][0])+':'+str(key_list[sbox-1][i][1]))
		f_key.write("\n")
	f_key.close()				


key_list = []
for i in range(8):
	key_list.append(make_key_list())

divide_input_and_output()
