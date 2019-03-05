# from des import *
# from find_key import *
import os

PC1 = [57, 49, 41, 33, 25, 17, 9, 1,
	58, 50, 42, 34, 26, 18, 10, 2,
	59, 51, 43, 35, 27, 19, 11, 3, 
	60, 52, 44, 36, 63, 55, 47, 39, 
	31, 23, 15, 7, 62, 54, 46, 38,
	30, 22, 14, 6, 61, 53, 45, 37, 
	29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
	15, 6, 21, 10, 23, 19, 12, 4,
	26, 8, 16, 7, 27, 20, 13, 2,
	41, 52, 31, 37, 47, 55, 30, 40,
	51, 45, 33, 48, 44, 49, 39, 56,
	34, 53, 46, 42, 50, 36, 29, 32]

missing_bit = [9, 18, 22, 25, 35, 38, 43, 54, 23, 19, 12, 4, 26, 8]		# The locations of missing bits that were not used in PC2
missing_keybits = [23, 19, 12, 4, 26, 8]

## Final key 42 bit
key42 = '000000000000000000111111111111111111000000' 
# print(key42)    
key42 = list(key42)
# print(key42)
key48 = key42[:12] + ['0'] * 6 + key42[12:]
# print(key48)

# Right rotate list 'l' by 'n' elements
def rotate(l, n):				
    return l[28-n:] + l[:28-n]

# returns possible 48 bit key lists
# def brute_forceKey48():
# 	res = []
# 	key48_list = []
# 	for i in range(64):		
# 		tmp=bin(i)[2:]
# 		while len(tmp) < 6:
# 			tmp = "0" + tmp
# 		res.append(list(tmp))
# 	# print(res)
# 	tmp_key48 = key42[:12] + [0]*6 + key42[12:]
# 	print("tmp key48 is ",tmp_key48)
# 	for i in range(len(res)):
# 		for j in range(len(res[i])):
# 			tmp_key48[missing_Sboxbits[j]-1] = res[i][j]
# 			key48_list.append(tmp_key48.copy())

# 	print("\n",key48_list)		
# 	return key48_list		

# Generate possible values for the missing bits
def generate_bruteforce_values():      
	res = []
	for i in range(16384):		# 2^ 14
		tmp=bin(i)[2:]
		while len(tmp) < 14:
			tmp = "0" + tmp
		res.append(list(tmp))
	# print(res[0])
	return res


def findKey56(key48):
	key56 = [0] * 56		# key is a 56 bit list
	k = 0
	for i in PC2:
		key56[i-1] = key48[k]
		k += 1
	return key56	

# Generate all possible 56 bit keys
def generate_56bit_keylist():			
	key56 = findKey56(key48)		# key56 is a bitlist with missing bits as 0
	keys_list = []
	res = generate_bruteforce_values()
	for i in range(len(res)):
		for j in range(len(res[i])):
			key56[missing_bit[j]-1] = res[i][j]
		keys_list.append(key56.copy())
	# print(keys_list[0])
	return keys_list		#returns a list of 56 bit keys [each key being in the form of bit list]		


def round1Key():
	keys_list = generate_56bit_keylist()
	round1_keylist = []
	for key in keys_list:
		# No rotation needed as it is the first round key for decryption
		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round1_keylist.append(round_key)
	return round1_keylist

def round2Key():
	keys_list = generate_56bit_keylist()
	round2_keylist = []
	for key in keys_list:
		key_left = key[:28]
		key_right = key[28:]
		res_left = rotate(key_left, 2)
		res_right = rotate(key_right, 2)
		res = res_left + res_right

		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round2_keylist.append(round_key)
	return round2_keylist

def round3Key():
	keys_list = generate_56bit_keylist()
	round3_keylist = []
	for key in keys_list:
		key_left = key[:28]
		key_right = key[28:]
		res_left = rotate(key_left, 4)
		res_right = rotate(key_right, 4)
		res = res_left + res_right

		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round3_keylist.append(round_key)
	return round3_keylist	

def round4Key():
	keys_list = generate_56bit_keylist()
	round4_keylist = []
	for key in keys_list:
		key_left = key[:28]
		key_right = key[28:]
		res_left = rotate(key_left, 6)
		res_right = rotate(key_right, 6)
		res = res_left + res_right

		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round4_keylist.append(round_key)
	return round4_keylist	

def round5Key():
	keys_list = generate_56bit_keylist()
	round5_keylist = []
	for key in keys_list:
		key_left = key[:28]
		key_right = key[28:]
		res_left = rotate(key_left, 8)
		res_right = rotate(key_right, 8)
		res = res_left + res_right

		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round5_keylist.append(round_key)	
	return round5_keylist

def round6Key():
	keys_list = generate_56bit_keylist()
	round6_keylist = []
	for key in keys_list:
		res = []
		# print(key)
		key_left = key[:28]
		key_right = key[28:]
		res_left = rotate(key_left, 9)
		res_right = rotate(key_right, 9)
		res = res_left + res_right

		round_key = [0] * 48
		k = 0
		for j in PC2:
			round_key[k] = res[j-1]
			k += 1
		round6_keylist.append(round_key.copy())	
	return round6_keylist			

# round1Key()
# round2Key()
# round3Key()
# round4Key()
# round5Key()
# round6Key()

# generate_56bit_keylist()