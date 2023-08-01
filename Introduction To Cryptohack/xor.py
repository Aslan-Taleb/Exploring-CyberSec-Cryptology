#Xor it's 1 when different and 0 when same

#to use xor
from pwntools  import  *
#we have a string with a integer
string_data = "label"
integer_data = 13
# we xor each letter with the number 13 
unicode_data = [xor(13,ord(i)) for i in string_data]
#then we get our flag ! 
print(unicode_data)

