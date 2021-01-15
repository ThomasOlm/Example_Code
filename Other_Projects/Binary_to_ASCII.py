## This program is meant to read a data in an outside file, convert it to ASCII text and output it

output_file = open("inputtext.txt", "r")
data = output_file.read()

def binary_to_ascii(data):

    ## break the data into 8 bit chunks

    sub_list = ""
    data_list = []
    counter = 0

    for char in data:

        sub_list = sub_list + char
        counter += 1

        if counter % 8 == 0 and counter != 0:

            data_list.append(sub_list)
            sub_list = ""
            counter = 0

    ## convert each 8 bit chunk into a decimal
    decimal_conversion = 0
    data_list_decimals = []

    for octect in data_list:

        counter = 7

        for char in octect:

            if char == "1":
                decimal_conversion += 2 ** counter
            counter -= 1

        data_list_decimals.append(decimal_conversion)
        decimal_conversion = 0

    ## convert each decimal to ascii char, python has a built in function for this
    data_list_ascii = []
    for num in data_list_decimals:
        data_list_ascii.append(chr(num))

    return ''.join(data_list_ascii)

print (binary_to_ascii(data))
