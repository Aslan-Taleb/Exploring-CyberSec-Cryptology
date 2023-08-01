#we want to use cryptosystems on our message
#but it's caractere so
#we convert each caractere to ascii number
#then to hex numbers then we concatenante
#then we can have it on base 16 or base 10
from Crypto.Util.number import *
# L'entier donné
entier = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convertir l'entier en bytes
bytes_data = long_to_bytes(entier)

# Convertir les bytes en message (chaîne de caractères)
flag = bytes_data.decode('utf-8')

print(flag)