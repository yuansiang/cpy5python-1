# ascii.py

# ASCII decimal to character
#for i in range(65,123): # uppercase A to lowercase z
#    print(chr(i)) # chr() returns ASCII character

# ASCII character to decimal
#print(ord('A'))

# Unicode hexadecimal to character
print(chr(0x5fb7))

# Unicode character to hexadecimal
print(hex(ord('德')))

# Dunman High School
##print(hex(ord('德')))
##print(hex(ord('明')))
##print(hex(ord('政')))
##print(hex(ord('府')))
##print(hex(ord('中')))
##print(hex(ord('学')))
print(chr(0x5fb7) + chr(0x660e) + chr(0x653f) + chr(0x5e9c) + chr(0x4e2d) + chr(0x5b66))