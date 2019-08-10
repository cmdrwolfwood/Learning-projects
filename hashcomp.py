#This script will compare 2 strings to check that they are the same,
# primarily for comparing hashes for data integrity.
def hashcomp():
     str1 = input("Input one:")
     str2 = input("Input two:")
     if str1 == str2:
        print("These input values are the same.")
     else:
        print("These input values are NOT the same.")

hashcomp()