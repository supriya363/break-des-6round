# from inspect import *
from des import *
import os
import sys
from collections import Counter

thirtybit_keylist = []		# global list will store all the possibilities 

def make_key_list():	# Returns list of all possible 64 keys[6 bits]
	key_list=[]
	for i in range(64):
		tmp=bin(i)[2:]
		while len(tmp) < 6:
			tmp = "0" + tmp
		key_list.append([tmp,0])
	return key_list

key_list = []
for i in range(8):
	key_list.append(make_key_list())

def getFrequencyOfKeys(thirtybit_keylist):
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
                    u1_possibility.append(sixBitInput1);
                if(val == output2):
                    rowIndexB = "{:02b}".format(rowIndex);
                    valB = "{:04b}".format(i);
                    sixBitInput2 = rowIndexB[0] + valB + rowIndexB[1];
                    u2_possibility.append(sixBitInput2);


        for u1 in u1_possibility:
            for u2 in u2_possibility:
                u1u2_xor = xor(u1, u2);
                u1u2_xor = ''.join(u1u2_xor);
                if(input_xor_val == u1u2_xor):
                    u1_str = [str(i) for i in u1];
                    u2_str = [str(i) for i in u2];
                    input_pairs.append([u1_str,u2_str]);

    return input_pairs;

def print_sbox_xor(xor_list):  #Testing
	sbox_count = 1
	for _xor in xor_list:
		if sbox_count != 1 and sbox_count != 3 and sbox_count != 4:
			print("Sbox {0} : {1}\n".format(sbox_count, _xor))
		sbox_count +=1



#output_pairs => dictionary index=> {[0,1,1,1],[1,1,1,1]}
def divide_input_and_output():
	if os.path.isfile('inputxor.txt') and os.path.isfile('outputxor.txt'):
		f_inp = open('inputxor.txt','r')
		f_out = open('outputxor.txt','r')
		f_r5 = open('expandr5.txt','r')
		
		inputxor_list = []
		outputxor_list = []
		count = 1
		for line_inp, line_out, line_r5 in zip(f_inp,f_out, f_r5): #line_inp = inputxor, line_out = outputxor
			inputxor_list = [ line_inp[i:i+6] for i in range(0,len(line_inp)-1,6)]
			outputxor_list = [ line_out[j:j+4] for j in range(0,len(line_out)-1,4)]
			r5_cipher1 = line_r5[:48]
			r5_cipher2 = line_r5[48:-1]
			sbox_keylist = []
			sbox = 1
			for input_xor,output_xor in zip(inputxor_list,outputxor_list):
				if sbox != 1 and sbox != 3 and sbox != 4:
					output_pairs = output_possibilities(output_xor)
					input_pairs = input_xor_possibilities(input_xor, output_pairs, sbox)
					sbox_keylist = find_key_possibilities(input_pairs, r5_cipher1, sbox, sbox_keylist, r5_cipher2 )
				sbox+=1
	else:
		print("No input file found here\n")
		raise SystemExit

def findKey30(keys_of_sboxes):
	count = 0
	thirty_bit_key = []
	print(keys_of_sboxes)
	for key0 in keys_of_sboxes[0]:
		for key1 in keys_of_sboxes[1]:
			for key2 in keys_of_sboxes[2]:
				for key3 in keys_of_sboxes[3]:
					for key4 in keys_of_sboxes[4]:
						thiry_bits_key_str = key0 + key1 + key2 + key3 + key4;
						thirty_bit_key.append(thiry_bits_key_str);
						count += 1;
	return thirty_bit_key

def find_key_possibilities(input_pairs, r5_cipher1, sbox, sbox_keylist, r5_cipher2):
	res = []

	for i in range(len(input_pairs)):
		start_index = (sbox-1)*6
		end_index = (sbox-1)*6+6
		key_from_u1 = xor(input_pairs[i][0], r5_cipher1[start_index: end_index])
		key_u1_str = ''.join(key_from_u1)
		res.append(key_u1_str)

	
	sbox_keylist.append(res)		# list having possible keys from all 5 sbox 
	if sbox == 8:
		flag = 0 
		for i in sbox_keylist:
			if not i:
				flag = 1
				break
		if flag != 1:
			tmp_list = findKey30(sbox_keylist)
			for i in tmp_list:
				thirtybit_keylist.append(i)		# In thirtybit_keylist count the frequency 
	return sbox_keylist				

def find_key_possibilities2(input_pairs, r5_cipher1, sbox, r5_cipher2):
	f_key = open('keyset'+str(sbox)+'.txt','w+')
	for i in range(len(input_pairs)):
		start_index = (sbox-1)*6
		end_index = (sbox-1)*6+6
		key_from_u1 = xor(input_pairs[i][0], r5_cipher1[start_index: end_index])
		key_from_u2 = xor(input_pairs[i][1], r5_cipher2[start_index: end_index])
		key_u1_str = ''.join(key_from_u1)
		key_u2_str = ''.join(key_from_u2)
		key_to_index = int(key_u1_str, 2)
		key_list[sbox-1][key_to_index][1] += 1 #[1] is the count of key at [0]
		for i in range(64):
			key_value = str(key_list[sbox-1][i][0])
			key_count = str(key_list[sbox-1][i][1])
			f_key.write(key_value+':'+key_count+'\n')
	f_key.close()
			


key_list = []
for i in range(8):
	key_list.append(make_key_list())

## Testing
divide_input_and_output()
# for i in thirtybit_keylist:
# 	print(i)

# frequency_of_keys = getFrequencyOfKeys(thirtybit_keylist)
# print(frequency_of_keys)
frequency_of_keys = getFrequencyOfKeys(thirtybit_keylist)
# print(frequency_of_keys.most_common())
uniquekeys = list(frequency_of_keys);
print(len(uniquekeys),sum(frequency_of_keys.values()));
f = open("Repeated_cipher_pairs.txt",'w+');
f.write(str(frequency_of_keys.most_common()[:50]));
f.close();