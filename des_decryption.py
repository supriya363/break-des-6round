from des import *
from generate_roundkeys import *
from generate_textstrings import alphabet_map, create_alphabet_map, bit_set

def create_reverse_map():
  global reverse_map
  k=0
  for i in bit_set:
    reverse_map[i]=input_set[k]
    k = (k+1)%16

def convert_bitstr_to_string(cipheredBits):
  mapBittoString = "";
  for i in range(0,16):
    fourBitString = cipheredBits[(i*4) : ((i*4)+4)]
    mapBittoString =mapBittoString + reverse_map[fourBitString];
  print(mapBittoString, len(mapBittoString))
  return mapBittoString



#convert the string "ffffffff" to corresponding bitstring
def convert_string_to_bitstring(ciphertext):
  create_alphabet_map(0)
  cipher_str = [ alphabet_map[ch] for ch in ciphertext]
  cipher_bitstring = ''.join(cipher_str)
  return cipher_bitstring



# 'i' is iterable. Assign it a value between 0-256 to get that particular combination
#key is a 56bit string. Get 6 round keys in order k6,k5,k4,k3,k2,k1

def get_round_keys(key, i):
  #TODO
  key_list = []
  key_list.append(round6Key()[i])
  key_list.append(round5Key()[i])
  key_list.append(round4Key()[i])
  key_list.append(round3Key()[i])
  key_list.append(round2Key()[i])
  key_list.append(round1Key()[i])
  # print(key_list)
  key_list = convert_to_str(key_list)
  return key_list


def func(input_text, key):
  exp_output = expansion(input_text)
  sbox_input = xor(key, exp_output)
  sbox_output = substitute(sbox_input)
  perm_output = permute(sbox_output)
  return perm_output

def round(right, left, key):
  func_output = func(left, key)
  next_left = xor(func_output, right)
  next_right = left
  return (next_right, next_left)

def getleft(cipher):
  return cipher[32:]  


def getright(cipher):
  return cipher[:32]

def decryption(ciphertext, key):
  cipher_bit_str = convert_string_to_bitstring(ciphertext)  #ciphert is a string 0001110101011
  round_keys = get_round_keys(key)
  cipher = initial_permutation(list(ciphert)) 
  left = list(getleft(''.join(cipher)))
  right = list(getright(''.join(cipher)))

  for round_no in range(6):
    (right, left) = round(right, left, round_keys[round_no])

  plaintext = final_permutation(left + right)
  return convert_bitstr_to_string(''.join(plaintext))

create_reverse_map()

key = ""
ciphertext = ""
plain_text = decryption(ciphertext, key)
print(plaintext)

