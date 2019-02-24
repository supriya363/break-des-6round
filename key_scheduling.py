from des import *
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

missing_bit = [9, 18, 22, 25, 35, 38, 43, 54]		# The locations of missing bits that were not used in PC2

# Left rotate list 'l' by 'n' elements
def rotate(l, n):				
    return l[n:] + l[:n]

# Generate possible values for the missing bits
def generate_bruteforce_values():      
	res = []
	for i in range(256):
		tmp=bin(i)[2:]
		while len(tmp) < 8:
			tmp = "0" + tmp
		res.append(list(tmp))
	print(res)
	return res	

# Computes the 56 bit key given as input to the first round. Input is bit list.
def undo_allround(key56):		
	res = []
	key56_left = key56[:28]
	key56_right = key56[28:]
	rotate(key56_left, 18)   #18 because upto 6 rounds there will be 1+1+2+2+2+2 left rotations, So we can reverse them by rotating again for 28-10 bits. 
	rotate(key56_right, 18)
	res = key56_left + key56_right
	return res

# Compute possible 56 bit keys using 48 bit 'key' and Input should be a bit list
def find_key56(key):		 
	key56 = [0] * 56		# key56 is a bit list
	k = 0
	for i in PC2:
		key56[i-1] = key[k]
		k += 1
	# print(key56)			# Initial key with missing bits as 0.

	# Using brute force we have to choose 6more bits 
	# The bits that are not used in PC2 are 9,18,22,25,35,38,43,54
	if os.path.isfile('possible_key.txt'):
		os.remove('possible_key.txt')
	f = open('possible_key.txt', 'a+')
	res = generate_bruteforce_values()
	for i in range(len(res)):
		for j in range(len(res[i])):
			key56[missing_bit[j]-1] = int(res[i][j])
		f.write(str(undo_allround(key56)))		# For some possible value of missing bits, finding the original 56bit key.
		f.write("\n")

	f.close()

a = [1]*48		# test input key 
find_key56(a)
