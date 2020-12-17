## making a variable length caesar cipher

def my_caesar(strng, num):
    encoded_strng = ""
    for char in strng:

        if ord(char) >= 65 and ord(char) <= 90:

            if ord(char) + num <= 90:
                encoded_strng += chr(ord(char) + num)

            else:
                encoded_strng += chr(ord(char) + num - 26)

        elif ord(char) >= 97 and ord(char) <= 122:

            if ord(char) + num <= 122:
                encoded_strng += chr(ord(char) + num)

            else:
                encoded_strng += chr(ord(char) + num - 26)

        else:
            encoded_strng += char

    return encoded_strng

string_to_encode = input("Enter string: ")
num_length = int(input("enter rotations: "))

print(my_caesar(string_to_encode, num_length))
