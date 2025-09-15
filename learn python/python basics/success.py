
binary_str = ' '.join([bin(b)[2:].zfill(8) for b in "DREAM BRO".encode('utf-8')])
print(binary_str)

binary_int = int(''.join(binary_str.split()), 2)
print(binary_int)