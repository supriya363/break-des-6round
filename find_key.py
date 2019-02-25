# from inspect import *
from des import *
import os
import sys
from collections import Counter

thirtybit_keylist = []		# global list will store all the possibilities 

key_list = []
for i in range(8):
	key_list.append(make_key_list())

def getFrequencyOfKeys(thirtybit_keylist):
    # count = 0
    # thirty_bit_key = []
    # for key0 in keys_of_sboxes[0]:
    #     for key1 in keys_of_sboxes[1]:
    #         for key2 in keys_of_sboxes[2]:
    #             for key3 in keys_of_sboxes[3]:
    #                 for key4 in keys_of_sboxes[4]:
    #                     thiry_bits_key_str = key0 + key1 + key2 + key3 + key4;
    #                     thirty_bit_key.append(thiry_bits_key_str);
    #                     count += 1;
    frequency_of_key = Counter(thirtybit_keylist)
    return frequency_of_key;

def xor(input1, input2):
	res = []
	for i in range(len(input1)):
		xorval = (ord(input1[i])-ord('0'))^(ord(input2[i])-ord('0'))
		res.append(chr(xorval+ord('0')))
	return res

def convBitList2Int(bitList):
    return int("".join(str(i) for i in bitList),2)

def output_possibilities(output_xor):  
	output_pairs = {}  # {[0,0,0,0]:[0,0,0,0] , [1,0,0,1]: [1,0,1,0]}
	for i in range(0,16):
		input_ = [int(x) for x in '{:04b}'.format(i)];
		input1 = [ str(i) for i in input_]
		input2 =  xor(input1, output_xor);
		output_pairs[convBitList2Int(input2)] = [input1,input2]
	return output_pairs

def make_key_list():	# Returns list of all possible 64 keys[6 bits]
	key_list=[]
	for i in range(64):
		tmp=bin(i)[2:]
		while len(tmp) < 6:
			tmp = "0" + tmp
		key_list.append([tmp,0])
	return key_list

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
		count = 1
		for line_inp, line_out, line_r5 in zip(f_inp,f_out, f_r5):
			j = 0
			inputxor_list = [ line_inp[i:i+6] for i in range(0,len(line_inp)-1,6)]
			outputxor_list = [ line_out[j:j+4] for j in range(0,len(line_out)-1,4)]
			r5 = line_r5[:48]
			
			sbox_keylist = []
			sbox = 1
			for input_xor,output_xor in zip(inputxor_list,outputxor_list):
				
				if sbox != 1 and sbox != 3 and sbox != 4:
					# print(sbox)
					output_pairs = output_possibilities(output_xor)
					input_pairs = input_xor_possibilities(input_xor, output_pairs, sbox)
					# if count < 18:
						# print(count)
					sbox_keylist = find_key_possibilities(input_pairs, r5, sbox, sbox_keylist)
					# count+=1
				sbox+=1
	else:
		print("No input file found here\n")
		raise SystemExit

def findKey30(keys_of_sboxes):
	count = 0
	thirty_bit_key = []
	for key0 in keys_of_sboxes[0]:
		for key1 in keys_of_sboxes[1]:
			for key2 in keys_of_sboxes[2]:
				for key3 in keys_of_sboxes[3]:
					for key4 in keys_of_sboxes[4]:
						thiry_bits_key_str = key0 + key1 + key2 + key3 + key4;
						thirty_bit_key.append(thiry_bits_key_str);
						count += 1;
	return thirty_bit_key

def find_key_possibilities(input_pairs, r5, sbox, sbox_keylist):
	f_key = open('keyset'+str(sbox)+'.txt','w+')
	# print(len(input_pairs))

	res = []
	for i in range(len(input_pairs)):
		res.append(''.join(xor(input_pairs[i][0], r5[(sbox-1)*6:(sbox-1)*6+6])))
	# print(res)		# res stores 6 bit key possibilty for 'sbox' passed 
	
	sbox_keylist.append(res)		# list having possible keys from all 5 sbox 
	# print("\n")
	# print(sbox_keylist)

	if sbox == 8:
		flag = 0 
		for i in sbox_keylist:
			if not i:
				# print("one of the input is empty")
				flag = 1
				break

		if flag != 1:
			tmp_list = findKey30(sbox_keylist)
			for i in tmp_list:
				thirtybit_keylist.append(i)		# In thirtybit_keylist count the frequency 
	f_key.close()
	return sbox_keylist				


divide_input_and_output()
for i in thirtybit_keylist:
	print(i)

# print(thirtybit_keylist)
frequency_of_keys = getFrequencyOfKeys(thirtybit_keylist)
print(frequency_of_keys)