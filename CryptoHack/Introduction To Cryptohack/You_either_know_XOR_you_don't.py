from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# it says 'myXORke+y...'
xor(flag, 'crypto{'.encode())
# trying until it's work
print(f"The Flag : {xor(flag, 'myXORkey'.encode())}") 
