## simple program to work with opening and closing files along with lambda functions 

from os import strerror

try:


    histogram = {}
    s = open('test.txt', "rt")
    ch = s.read(1)

    while ch != '':
        ch = ch.lower()

        if ch in histogram:
            histogram[ch] = int(histogram.get(ch)) + 1
        else:
            histogram[ch] = 1

        ch = s.read(1)

    s.close()

    histogram = {key: value for key, value in reversed(sorted(histogram.items(), key=lambda item: item[1]))}

    print("\n\nCharacters in file:", histogram)

    new_file = open("test.hist", "w")
    for key in histogram:

        string = ""
        string = string + str(key) + " -> " + str(histogram[key]) + "\n"

        new_file.write(string)

    new_file.close()

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
