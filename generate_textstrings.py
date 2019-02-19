from des import *
import itertools
import sys
import os

input_set = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
left_xor = ['0100','0000','0101','1010','0000','0000','0000','0000']
right_xor = ['0000','0100','0000','0000','0000','0000','0000','0000']

# Finds the corresponding input having the required xor difference
# inp is in the form - "8 chars"
def findPair(inp, xor):     
    res = []
    tmp = list(inp)
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
    return L_20 + R_20        

# Storing the plaintext pairs in the file 'input.txt' in the form 'plaintext1,plaintext2'
def input_pairs():
    if os.path.isfile('input.txt'):
        os.remove('input.txt')
        
    f = open('input.txt','w')
    count = 0
    for p in itertools.product(input_set, repeat=8):
        if(count < 100):            # change the '1000000' to the number of pairs of plaintext needed.
            f.write("ffffffff"+''.join(p)+",")
            f.write(generate_pair("ffffffff"+''.join(p)))
            f.write("\n")
            count += 1    
        else:
            f.close()
            raise SystemExit
    
    f.close()

#Generate Pairs    
input_pairs()
