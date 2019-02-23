from des import *
import itertools
import sys
import os

input_set = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
left_xor = ['0100','0000','0101','1010','0000','0000','0000','0000']
right_xor = ['0000','0100','0000','0000','0000','0000','0000','0000']
bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
alphabet_map = {}
R5XOR = "405A0000" #Not required

def create_alphabet_map():
	global alphabet_map
	k=0
	for i in input_set:
		alphabet_map[i]=bit_set[k]
		k+=1

# Finds the corresponding input having the required xor difference
# inp is in the form - "8 chars"
def findPair(inp, xor):     
    res = []
    tmp = list(inp)
    # print(tmp)
    for i in range(len(tmp)):
        x = bin(int(binvalue(tmp[i],8), 2) - int(binvalue("f",8),2))[2:]
        y = int(x,2) ^ int(xor[i],2)
        res.append(input_set[y])
    res = ''.join(res)
    return res

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
        
    f = open('input.txt','w')
    count = 0
    for p in itertools.product(input_set, repeat=8):
        if(count < 10):            # change the '1000000' to the number of pairs of plaintext needed.
            f.write("ffffffff"+''.join(p)+",")
            f.write(generate_pair("ffffffff"+''.join(p)))
            f.write("\n")
            count += 1    
        else:
            f.close()
            # raise SystemExit
            break
    
    f.close()

#generates new input-output bitencoded files which have apprpriate xor in the last round
def clean_input_output_pairs():
	if os.path.isfile('outputcipher.txt'):  #contains bit-encoded ciphertext pairs
		f_out = open('outputcipher.txt','r') 
		f_inp = open('outputplain.txt','r') #contains bitencoded plaintext pairs
		f_clean_inp = open('output_plain_clean.txt','w')
		f_clean_out = open('ouput_cipher_clean.txt','w')
		for line_out,line_inp in zip(f_out,f_inp):

			# get l6xor, since l6xor = r5xor, remove the input-output pairs
			# that don't have lrxor same as our calculated r5xor
			diff = get_diff_of_cipherpair(line_out[:64],line_out[65:-1])[:32]
			# print(convert_input_to_xor(list(diff)))

			r5_xor_bitarr = convert_xor_to_input(R5XOR)  #convert from hex
			r5_xor_bitval = ''.join(r5_xor_bitarr)
			if diff == r5_xor_bitval:
				f_clean_inp.write(line_inp[:64]+' '+line_inp[65:-1]+'\n')
				f_clean_out.write(line_out[:64]+' '+line_out[65:-1]+'\n')

def get_diff_of_cipherpair(left, right):
	left_bitarr = list(left)
	right_bitarr = list(right)
	diff_bitarr = xor(left_bitarr, right_bitarr)
	return ''.join(diff_bitarr)		

#convert text pairs to bit strings - save them in outputplain.txt/outputcipher.txt
def convert_pairs_to_bitstring(flag):
	if flag == 'p': #Not Required
		if os.path.isfile('input.txt'):
			f1 = open('input.txt','r')
			f2 = open('outputplain.txt','w')
		else:
			print("No input pair file found\n")
			raise SystemExit
	elif flag == 'c':
		if os.path.isfile('cipherpair.txt'):
			f1 = open('cipherpair.txt','r')
			f2 = open('cipher.txt','w')
		else:
			print("No input file found")
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
input_pairs()
create_alphabet_map()
convert_pairs_to_bitstring('p')
convert_pairs_to_bitstring('c')





