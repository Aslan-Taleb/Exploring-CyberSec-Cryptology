
encrypted_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encrypted = bytes.fromhex(encrypted_hex)

def xor_single_byte(key, data):
    return bytes(byte ^ key for byte in data)

def is_crypto(text):
        search_text = "crypto"
        search_bytes = search_text.encode('utf-8')
        if search_bytes in text:
             return True
        else:
             False

for key in range(256):  # Try all possible single-byte keys (from 0 to 255)
    decrypted = xor_single_byte(key, encrypted)
    if is_crypto(decrypted):
        print(f"The key is : {key}, Decrypted text: {decrypted}")
