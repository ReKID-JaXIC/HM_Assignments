#Task 1 ##############################
temp_num = 18
print(temp_num, bin(temp_num), hex(temp_num))
#Task 2 ###################################
#TypeError: 'float' object cannot be interpreted as an integer
#Task 3 ####################################
bin_num = 0b1011
hex_num = 0xA3
print(bin_num, hex_num)
#Task 4 ######################################
full_sum = temp_num + bin_num + hex_num
print("The sum is ", full_sum)
#Task Compression ##############################
#Numbers were generated randomly from 1 to 2^64,
# the trailing zeroes may have been due to inaccuracy with the RNG function on the website used
comp_size = 5582168342022468000
dict_size = 1681050344375599000
orig_size = 12119989121067004000
percentage = 1 - ((comp_size + dict_size) / orig_size)
print(f"Original Size: {orig_size} Characters\nCompressed Size: {comp_size} Characters\n"
      f"Dictionary Size: {dict_size} Characters\nCompression Percentage: {percentage * 100}%")