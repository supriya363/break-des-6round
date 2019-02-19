from boxes import *

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

#Should return bit array
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
        # print(outputOfSBox)
    return list(outputOfSBox)

def xor(input1, input2):
	res = []
	for i in range(len(input1)):
		xorval = (ord(input1[i])-ord('0'))^(ord(input2[i])-ord('0'))
		res.append(chr(xorval+ord('0')))
	return res


def permute(inp):
	res = [0]*32
	k = 0
	for i in PBOX:
		res[k] = inp[i-1]
		k+=1
	return res

def inverse_permute(inp):
	pass



def binaryToHex(val):
    return hex(int(''.join(val),2))[2:]

def hexToBinary(inp):
    res = bin(int(''.join(inp), 16))[2:]
    while (len(res) < 4):
        res = '0' + res
    return res

def convert_xor_to_input(inp):   #e.g. inp = "0405C000" 
	arr = list(inp)
	res = []
	for i in arr:
		tmp = list(hexToBinary(i))
		for j in range(len(tmp)):
			res.append(tmp[j])
			# res = expansion(res)        #converting the 32 bit input to 48 bit  
	return res

def convert_input_to_xor(inp):   # Converts 32bit input to xor (e.g. 0405C000)
    res = []
    for i in range(0,len(inp),4):
        res.append(binaryToHex(inp[i:i+4]))
    return ''.join(res)

def round(li, ri, no_of_rounds):
	for rnd in range(no_of_rounds):
		print("----------------------Round---------------------- : %d\n" % (rnd+1))
		print("Lefthalf: "+ str(li) + "\nRighthalf: " + str(ri))
		expansion_output = expansion(ri)
		substitute_output = substitute(expansion_output) #need to take care of xor
		permutation_output = permute(substitute_output)
		print("After expansion: "+str(expansion_output))
		print("After Substitution" + str(substitute_output))
		print("After Permutation"+str(permutation_output))
		print("After expansion: "+str(convert_input_to_xor(expansion_output)))
		print("After Substitution: " + str(convert_input_to_xor(substitute_output)))
		print("After Permutation: "+str(convert_input_to_xor(permutation_output)))
		xor_with_lefthalf = xor(permutation_output, li)
		print("After Xoring with left half: " + str(convert_input_to_xor(xor_with_lefthalf)))
		print("\n")
		li = ri
		ri = xor_with_lefthalf

def getinputXor(leftXOR,rightXOR):

	left = convert_xor_to_input(leftXOR)
	right = convert_xor_to_input(rightXOR)
	round(left, right, 1)



#taken from online resources
def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval



def roundTest():
	l = list("abcd") #64bits
	r = list("efgh")
	bval_l = [ binvalue(i,8) for i in l]
	bval_r = [ binvalue(i,8) for i in r]
	out_l = []
	out_r = []
	for i in bval_l:
		out_l.append(list(i))
	for i in bval_r:
		out_r.append(list(i))
	bitarr_l = []
	bitarr_r = []
	for ele in out_l:
		for j in ele:
			bitarr_l.append(j)
	for ele in out_r:
		for j in ele:
			bitarr_r.append(j)
	print("Input: " + str(bitarr_l)+str(bitarr_r))
	round(bitarr_l, bitarr_r, 2)



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





# roundTest()
getinputXor("00808200","60000000")

