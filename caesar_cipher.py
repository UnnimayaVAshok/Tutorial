message=input("Enter message:")
key=int(input("Enter the key:"))
ciphertext=""
for ch in message:
    ordinal_ch=ord(ch)
    ordinal_ch+=key
    if ordinal_ch>ord('z'):
        ordinal_ch=ord('a')+(ordinal_ch-ord('z')-1)
    newch=chr(ordinal_ch)
    ciphertext+=newch
print(ciphertext)

decrypted_message = ""

for ch in ciphertext:
    ordinal_ch = ord(ch)
    ordinal_ch -= key
    if ordinal_ch < ord('a'):
        ordinal_ch = ord('z') - (ord('a') - ordinal_ch - 1)
    new_ch = chr(ordinal_ch)
    decrypted_message += new_ch

print("Decrypted message:", decrypted_message)