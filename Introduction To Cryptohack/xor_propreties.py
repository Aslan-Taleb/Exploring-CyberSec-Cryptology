def xor(*args):
    result = args[0]
    for arg in args[1:]:
        result = bytes(a ^ b for a, b in zip(result, arg))
    return result

# Define the hex strings
key1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key_1_2_hex ="37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key2_3_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
key_1_2_3_flag_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key1 = bytes.fromhex(key1_hex)
key1_2 = bytes.fromhex(key_1_2_hex)
key2 = xor(key1,key1_2)
print(key2)

key2_3 = bytes.fromhex(key2_3_hex)
key3 = xor(key2_3,key2)
print(key3)

# Calculate the final flag
key_1_2_3_flag = bytes.fromhex(key_1_2_3_flag_hex)
flag = xor(key_1_2_3_flag,key1,key2,key3)
print(f"The Flag : {flag} ")


