encrypted_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encrypted = bytes.fromhex(encrypted_hex)

def is_crypto(text):
        search_text = "crypto"
        search_bytes = search_text.encode('utf-8')
        if search_bytes in text:
             return True
        else:
             False
all_possible_keys = [key for key in range(256)]
for i in all_possible_keys:
      
