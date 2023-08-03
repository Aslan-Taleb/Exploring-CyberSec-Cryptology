#we got integers we convert each one to the letter on the ascii table
integer = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
hex_data = [chr(i) for i in integer]
separator = ""
flag = separator.join(hex_data)
print(flag)