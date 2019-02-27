from des import *
import itertools
import sys
import os

input_set = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
#input xor required 0000801000004000
left_xor = ['0000','0000','0000','0000','1000','0000','0001','0000']  #00008010 
right_xor = ['0000','0000','0000','0000','0100','0000','0000','0000'] #00004000

#input xor required for 2nd trail
# left_xor = ['0000','0000','0000','0000','1000','0000','0001','0000']  #00008010 
# right_xor = ['0000','0000','0000','0000','0100','0000','0000','0000'] #00004000

bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
alphabet_map = {}




def create_alphabet_map(start):
	global alphabet_map
	k=start
	for i in input_set:
		alphabet_map[i]=bit_set[k]
		k = (k+1)%16

# Finds the corresponding input having the required xor difference
# # inp is in the form - "8 chars"
# def findPair(inp, xor):     
#     res = []
#     tmp = list(inp)
#     # print(tmp)
#     for i in range(len(tmp)):
#         x = bin(int(binvalue(tmp[i],8), 2) - int(binvalue("f",8),2))[2:]
#         y = int(x,2) ^ int(xor[i],2)
#         res.append(input_set[y])
#     res = ''.join(res)
#     return res

def findPair(inp, xor_list):
	# print(inp)
	tmp_list = list(inp)
	plaintext2 = []
	k = 0
	for i in tmp_list:
		t1 = list(alphabet_map[i])
		t2 = list(xor_list[k])
		# print(t1,t2)
		xor_result = xor(t1, t2)
		# print(xor_result)
		for j in alphabet_map:
			if alphabet_map[j] == (''.join(xor_result)):
				plaintext2.append(j)
				break
		k += 1 
	plaintext2 = ''.join(plaintext2)
	# print("plaintext2",plaintext2)
	return plaintext2	
	

# Returns the plaintext for the entered plaintext maintaining xor difference
# inp will be in the form - "16 chars : {L_0R_0}"
def generate_pair(inp):      
    L_10 = inp[:8]
    R_10 = inp[8:]
    L_20 = findPair(L_10, left_xor)
    R_20 = findPair(R_10, right_xor)
    # print(inp)
    return L_20 + R_20        

# Storing the plaintext pairs in the file 'input.txt' in the form 'plaintext1,plaintext2'
def input_pairs():
	if os.path.isfile('input.txt'):
		os.remove('input.txt')

	f = open('input.txt','w+')
	count = 0
	for p in itertools.product(input_set, repeat=8):
		if(count < 2000):       
			count += 1 
			f.write(''.join(p)+''.join(p)+",\n")
			f.write(generate_pair(''.join(p)+''.join(p)))
			f.write(",\n")
		else:
			break

	f.close()


def convert_responsefile_to_cipher():
	if os.path.isfile('response.txt'):
		f1 = open('response.txt','r')
		f2 = open('cipherpair.txt','w+')
		flag = 0
		for line in f1:
			if flag ==0:
				f2.write(line[:16])
				flag = 1
			else:
				f2.write(' ' + line[:16]+'\n')
				flag = 0
		f1.close()
		f2.close()
	else:
		print("No Responsefile.txt found")
		raise SystemExit


def get_diff_of_cipherpair(left, right):
	left_bitarr = list(left)
	right_bitarr = list(right)
	diff_bitarr = xor(left_bitarr, right_bitarr)
	return ''.join(diff_bitarr)		

#convert text pairs to bit strings - save them in outputplain.txt/outputcipher.txt
def convert_pairs_to_bitstring(flag):
	if flag == 'c':
		if os.path.isfile('cipherpair.txt'):
			f1 = open('cipherpair.txt','r')
			f2 = open('cipher.txt','w+')
		else:
			print("No input file cipherpair.txt found")
			raise SystemExit
	for line in f1:
		pair_first = line[:16]
		pair_second = line[17:-1]
		input1 = [ alphabet_map[ch] for ch in pair_first]
		input2 = [ alphabet_map[ch] for ch in pair_second]
		bit_string1 = ''.join(input1)
		bit_string2 = ''.join(input2)
		f2.write(bit_string1 + ' ' + bit_string2+ '\n')
	f1.close()
	f2.close()

#Generate Pairs  
# create_alphabet_map(1)
# print(alphabet_map)

#PHASE 1   
# input_pairs()



# PHASE 2 - After creation of Responsefile.txt
convert_responsefile_to_cipher()

# create_alphabet_map()
convert_pairs_to_bitstring('c')







