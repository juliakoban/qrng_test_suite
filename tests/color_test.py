import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
grid_size = 256  
total_bytes = grid_size * grid_size  

# BINARY FILE FROM QRNG
binary_file_path = '../data/QNGFile.dat' 
with open(binary_file_path, 'rb') as file:
    binary_data = file.read(total_bytes)
# Convert binary data to a binary string
binary_strings = ''.join(format(byte, '08b') for byte in binary_data)
bit_sequence = np.array([int(bit) for bit in binary_strings], dtype=np.uint8)
bit_grid_binary = bit_sequence[:grid_size ** 2].reshape((grid_size, grid_size))

# ASCII FILE
ascii_file_path = '../data/potter.txt' 
with open(ascii_file_path, 'r', encoding='utf-8') as file:
    ascii_data = file.read(total_bytes)
# Convert ASCII data to binary
binary_strings_ascii = ''.join(format(ord(char), '08b') for char in ascii_data)
bit_sequence_ascii = np.array([int(bit) for bit in binary_strings_ascii], dtype=np.uint8)  
bit_grid_ascii = bit_sequence_ascii[:grid_size ** 2].reshape((grid_size, grid_size))

# A color map (0 -> black, 1 -> white)
cmap = plt.cm.gray  

# RESULTS PLOTTING
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# BIINARY IMAGE
im_binary = axs[0].imshow(bit_grid_binary, cmap=cmap, interpolation='nearest')
axs[0].set_title("QRNG DATA IMAGE")
axs[0].axis('off')  
#plt.colorbar( im_binary, ax = axs[0] )  

# ASCII IMAGE
im_text = axs[1].imshow(bit_grid_ascii, cmap=cmap, interpolation='nearest')
axs[1].set_title("'HARRY POTTER' DATA IMAGE")
axs[1].axis('off')  
#plt.colorbar( im_text, ax = axs[1] )  

plt.tight_layout()
plt.show()