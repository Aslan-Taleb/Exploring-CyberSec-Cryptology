# Xor it's 1 when different and 0 when same

# To use xor (found on internet..)
def xor(*args):
    if all(isinstance(arg, int) for arg in args):
        # If all arguments are integers, convert them to a single-byte bytes object
        args = [bytes([arg]) for arg in args]
    elif not all(isinstance(arg, bytes) for arg in args):
        raise ValueError("All arguments must be either integers or bytes-like objects.")

    result = args[0]
    for arg in args[1:]:
        result = bytes(a ^ b for a, b in zip(result, arg))
    return result

# We have a string with an integer
string_data = "label"
integer_data = 13

# We xor each letter with the number 13
flag = [xor(integer_data, ord(i)) for i in string_data]
# Then we get our flag!
print(flag)
