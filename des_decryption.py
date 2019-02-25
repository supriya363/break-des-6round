# from des import *
from generate_roundkeys import *
from generate_textstrings import alphabet_map, create_alphabet_map, bit_set


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

#convert the string "ffffffff" to corresponding bitstring
def convert_string_to_bitlist(ciphertext):
  create_alphabet_map()
  cipher_str = [ alphabet_map[ch] for ch in ciphertext]
  cipher = ''.join(cipher_str)
  return cipher

# 'i' is iterable. Assign it a value between 0-256 to get that particular combination
#key is a 56bit string. Get 6 round keys in order k6,k5,k4,k3,k2,k1

def get_round_keys(key, i):
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

def convert_to_str(key_list):
  new_key_list = []
  for key in key_list:
    key_str = [ str(i) for i in key]
    new_key_list.append(key_str)
  return new_key_list


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
  ciphert = convert_string_to_bitlist(ciphertext)  #ciphert is a string 0001110101011
  round_keys = get_round_keys(key)
  cipher = initial_permutation(list(ciphert)) 
  left = list(getleft(''.join(cipher)))
  right = list(getright(''.join(cipher)))

  for rno in range(6):
    (right, left) = round(right, left, round_keys[rno])

  plaintext = final_permutation(right, left)
  return plaintext  #bitlist



# decryption('fghijklm', '0000000')

