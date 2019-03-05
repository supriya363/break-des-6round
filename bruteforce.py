#Due to lack of time we couldn't code the entire decryption and encryption ourselves so we took help from online resources to use some existing functionalities 
#and modified them according to our need

#Initial permut matrix for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

#Initial permut made on the key
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

#Permut applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

#Expand matrix to get a 48bits matrix of datas to apply the xor with Ki
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

#SBOX
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

#Permut made after each SBox substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

#Final permut for datas after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

#Matrix that determine the shift for each round of keys
SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def BruteForecedKeys():
    knownBits = [3, 44, 27, 17, 42, 10,26, 50, 60, 2, 41, 35,52, 59, 58, 49, 11, 34,13, 23, 30, 45, 63, 62,38, 21, 31, 12, 14, 55,20, 47, 29, 54, 6, 15,4, 5, 39, 53, 46, 22]
    unknownBits = [1,7,9,18,19,25,28,33,36,37,43,51,57,61]

    keyBits = [None] * 64

    foundKeysBits = [0,1,0,0,0,1,
                     1,0,1,1,0,1,
                     0,0,1,0,0,0,
                     1,0,1,1,1,1,
                     0,1,1,0,0,1,
                     1,0,0,1,0,0,
                     1,1,0,1,0,0]

    foundKeyIndex = 0
    for i in knownBits:
        keyBits[(i-1)] =foundKeysBits[foundKeyIndex]
        foundKeyIndex += 1;


    for i in range(1,9):
        parityBitIndex = (i * 8) -1;
        keyBits[parityBitIndex] = 0  #Setting all parity bits to be zero
#     print(keyBits)


    for index, val in enumerate(unknownBits):
        unknownBits[index] = val - 1;
#     print(keyBits)

#     print(unknownBits)
    bruteForcedKeys = []
    count = 0
    for one in (0,1):
        for two in (0,1):
            for three in (0,1):
                for four in (0,1):
                    for five in (0,1):
                        for six in (0,1):
                            for seven in (0,1):
                                for eight in (0,1):
                                    for nine in (0,1):
                                        for ten in (0,1):
                                            for eleven in (0,1):
                                                for twelve in (0,1):
                                                    for thirteen in (0,1):
                                                        for fourteen in (0,1):
                                                            keyBits[unknownBits[0]] = one
                                                            keyBits[unknownBits[1]] = two
                                                            keyBits[unknownBits[2]] = three
                                                            keyBits[unknownBits[3]] = four
                                                            keyBits[unknownBits[4]] = five
                                                            keyBits[unknownBits[5]] = six
                                                            keyBits[unknownBits[6]] = seven
                                                            keyBits[unknownBits[7]] = eight
                                                            keyBits[unknownBits[8]] = nine
                                                            keyBits[unknownBits[9]] = ten
                                                            keyBits[unknownBits[10]] = eleven
                                                            keyBits[unknownBits[11]] = twelve
                                                            keyBits[unknownBits[12]] = thirteen
                                                            keyBits[unknownBits[13]] = fourteen
#                                                             if count < 2:
#                                                                 doEncryption(keyBits)
#                                                             count += 1
                                                            doEncryption(keyBits)
                                                            bruteForcedKeys.append(keyBits);

    return bruteForcedKeys;

def string_to_bit_array(text):#Convert a string into a list of bits
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return array

def bit_array_to_string(array): #Recreate the string from the bit array
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   
    return res

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in range(0, len(s), n)]

ENCRYPT=1
DECRYPT=0

input_set = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
bit_set = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
reverse_map = {}

def create_reverse_map():
  global reverse_map;
  k=0
  for i in bit_set:
    reverse_map[i]=input_set[k]
    k = (k+1)%16
create_reverse_map()
def convert_bitstr_to_string(cipheredBits):
    mapBittoString = "";
    for i in range(0,16):
        fourBitString = cipheredBits[(i*4) : ((i*4)+4)]
        mapBittoString =mapBittoString + reverse_map[fourBitString];
    return mapBittoString



class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()
        
    def run(self, key, text, action=ENCRYPT, padding=False):
        self.password = key
        self.text = text
        
        if padding and action==ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:#If not padding specified data size must be multiple of 8 bytes
            raise "Data size should be multiple of 8"
        
        self.generatekeys() #Generate all the keys
        text_blocks = text;
        print(text_blocks, len(text_blocks))
        result = list()
        block = [int(m) for m in text_blocks]
        block = self.permut(block,PI)#Apply the initial permutation
        g, d = nsplit(block, 32) #g(LEFT), d(RIGHT)
        tmp = None
        for i in range(6): #Do the 16 rounds
            d_e = self.expand(d, E) #Expand d to match Ki size (48bits)
            if action == ENCRYPT:
                tmp = self.xor(self.keys[i], d_e)#If encrypt use Ki
            else:
                tmp = self.xor(self.keys[5-i], d_e)#If decrypt start by the last key
            tmp = self.substitute(tmp) #Method that will apply the SBOXes
            tmp = self.permut(tmp, P)
            tmp = self.xor(g, tmp)
            g = d
            d = tmp
        result += self.permut(d+g, PI_1)
            #Do the last permut and append the result to result
        return result
    
    def substitute(self, d_e):#Substitute bytes using SBOX
        subblocks = nsplit(d_e, 6)#Split bit array into sublist of 6 bits
        result = list()
        for i in range(len(subblocks)): #For all the sublists
            block = subblocks[i]
            row = int(str(block[0])+str(block[5]),2)#Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]),2) #Column is the 2,3,4,5th bits
            val = S_BOX[i][row][column] #Take the value in the SBOX appropriated for the round (i)
            bin = binvalue(val, 4)#Convert the value to binary
            result += [int(x) for x in bin]#And append it to the resulting list
        return result
        
    def permut(self, block, table):#Permut the given block using the given table (so generic method)
        return [block[x-1] for x in table]
    
    def expand(self, block, table):#Do the exact same thing than permut but for more clarity has been renamed
        return [block[x-1] for x in table]
    
    def xor(self, t1, t2):#Apply a xor and return the resulting list
        return [x^y for x,y in zip(t1,t2)]
    
    def generatekeys(self):#Algorithm that generates all the keys
        self.keys = []
#         key = string_to_bit_array(self.password)
        key = self.password;
#         print("Generate Key",key)
        key = self.permut(key, CP_1) #Apply the initial permut on the key
        g, d = nsplit(key, 28) #Split it in to (g->LEFT),(d->RIGHT)
        for i in range(6):#Apply the 16 rounds
            g, d = self.shift(g, d, SHIFT[i]) #Apply the shift associated with the round (not always 1)
            tmp = g + d #Merge them
            self.keys.append(self.permut(tmp, CP_2)) #Apply the permut to get the Ki
#         print('Keys of 6 th round',self.keys[5])

    def shift(self, g, d, n): #Shift a list of the given value
        return g[n:] + g[:n], d[n:] + d[:n]
    
    def addPadding(self):#Add padding to the datas using PKCS5 spec.
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)
    
    def removePadding(self, data):#Remove the padding of the plain text (it assume there is padding)
        pad_len = ord(data[-1])
        return data[:-pad_len]
    
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)
    
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)
    

def doEncryption(key):
    text= "ktlrlquttmgillot"
    text = convert_string_to_bitstring(text);
    
    d = des()
    r = d.encrypt(key,text)
    bit_string = ''.join(str(e) for e in r)
    cipher = convert_bitstr_to_string(bit_string)
    if cipher == "ikqllgnkqnjjognp":
        print('Key is ', key)
    
alphabet_map = {}

def create_alphabet_map(start):
    global alphabet_map
    k=start
    for i in input_set:
        alphabet_map[i]=bit_set[k]
        k = (k+1)%16

create_alphabet_map(0)


def convert_string_to_bitstring(plaintext):
  create_alphabet_map(0)
  plain_str = [ alphabet_map[ch] for ch in plaintext]
  plain_bitstring = ''.join(plain_str)
  return plain_bitstring
 
    
    

    

if __name__ == '__main__':
    text= "msiiokopiuhpjmhi"
    
    text = convert_string_to_bitstring(text);
    d = des()
    key = [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    r = d.decrypt(key,text)
    bit_string1 = ''.join(str(e) for e in r)
    cipher = convert_bitstr_to_string(bit_string)
    print(cipher)
    if cipher == "ikqllgnkqnjjognp":
        print('Key is ', key)
        
    text= "nfhshlmpsqisgisn"
    
    text = convert_string_to_bitstring(text);
    d = des()
    key = [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
    r = d.decrypt(key,text)
    bit_string2 = ''.join(str(e) for e in r)
    cipher1 = convert_bitstr_to_string(bit_string)
    cipher = cipher + cipher1
    print(cipher)
        
