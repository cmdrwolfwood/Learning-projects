#This script is designed to intake a hex string and output a converted string of
# base 64
import binascii
def hex2b64():
    r = bytes.fromhex(input("Input your hexadecimal string:"))
# bytes.fromhex converts the hex input to binary/bytes
# printing only the variable r would give you a decoded hex string
    b64string = binascii.b2a_base64(r)
# b2a_base64 converts binary/bytes to line of readable ascii in b64
    print ("Your base64 string is:")
    print(b64string)
    print("Ignore the b and /n characters.")

hex2b64()
