

#Permutation Box
PBOX = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Substitution Boxes
s1 = [ [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

s2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]


s3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
]

s4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ]

s5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3] ]

s6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ]

s7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

s8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

SBOX = [s1,s2,s3,s4,s5,s6,s7,s8]

def expansion(ri):  #ri is an array of bits = b0,b1,b2...b31
	res = []
	res.append(ri[31])
	res.append(ri[0])
	once = 1
	for i in range(1,31,2):
		if once == 1:
			res.append(ri[i])
			res.append(ri[i+1])
			once = 2
		else:
			for j in range(2):
				res.append(ri[i])
				res.append(ri[i+1])
			once = 1
	res.append(ri[31])
	res.append(ri[0])
	return res


def substitute(ei):
    outputOfSBox = ''
    for i in range(0,8):
        rowIndex_0bit = i * 6;
        rowIndex_1bit = rowIndex_0bit + 5
        rowIndex_bit = ei[rowIndex_0bit] + ei[rowIndex_1bit];
        rowIndex = int(rowIndex_bit,2)
        coulmnStartIndex = rowIndex_0bit +1;
        columnIndex = int(''.join(ei[coulmnStartIndex:rowIndex_1bit]),2)
        sBox = SBOX[i];
        #print(sBox[rowIndex][columnIndex], "{0:04b}".format(sBox[rowIndex][columnIndex]))
        outputOfSBox = outputOfSBox + "{0:04b}".format(sBox[rowIndex][columnIndex])
        #print(outputOfSBox)
    return outputOfSBox

def xor(input1, input2):
	res = []
	for i in range(len(input1)):
		res.append(input1[i]^input2[i])
	return res


def permute(inp):
	res = [0]*32
	print(inp[15])
	k = 0
	for i in PBOX:
		res[k] = inp[i-1]
		k+=1
	return res

def round(li, ri):
	pass

def func(ri):  #returns output xor
	pass


#taken from online resources
def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def convert_xor_to_input(inp):
	res = expansion(inp)
	arr = []		#list to store the inputs to S-box in the form ["b0 b1 b2 b3 b4 b5"]
	inp_length = 6		#Input length to S-box
	count = 1
	k = 0			
	for i in res:
		while(count <= inp_length):
			arr[k] = arr[k] + res[i+count]
			count = count+1
		k = k+1
		count = 1
		i = i + 6
		arr.append(arr[k])

	return arr

def testProg():
	inp = list("abcd") #32bits
	bval = [ binvalue(i,8) for i in inp]
	out = []
	for i in bval:
		out.append(list(i))
	bitarr = []
	for ele in out:
		for j in ele:
			bitarr.append(j)
	print("Input: " + str(bitarr))




testProg()
