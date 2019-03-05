# break-des-6round
Breaking 6 round DES using chosen plaintext attack

To run: 
#PHASE 1 : Go to generate_textstring.py
#Uncomment the following code to run Phase 1 - generate input pairs
# input_pairs()

#PHASE 2 - Run Response.py to get ciphertexts of the input pairs

#PHASE 3 - Uncomment the following lines in generate_textstring.py
convert_responsefile_to_cipher()
convert_pairs_to_bitstring('c')

#PHASE 4 - compute the input output xors into the sboxes in the last round
#Run compute_input_output_xor.py in order to do this

#PHASE 5 - Find key possibilities by running find_key.py

You can see the 30 bit key values in Repeated_cipher_pairs.txt. The one with the maximum frequency are the required key bits. 

