import base64
#basa64 used to represent binary data as an 
#we have Hex data encoded
hex_data = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
#we decoded into bytes
bytes_data = bytes.fromhex(hex_data)
#Then To Base64
flag = base64.b64encode(bytes_data)
print(flag)