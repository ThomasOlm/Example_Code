## program to read from a file and count the amount of points each person has. More practice working with exception clauses as well

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    # Write your code here.
    pass


class FileEmpty(StudentsDataException):
    # Write your code here.
    pass

try:

    histogram = {}


    s = open('test.txt', "rt")

    if s:
        pass

    else:
        raise FileEmpty("File is empty!")

    line = s.readline()

    if line:
        pass
    else:
        raise BadLine("Line is wrong")

    while line != '':

        listofitems = line.split("\t")


        if "\n" in listofitems[-1]:
            listofitems[-1] = listofitems[-1].strip("\n")

        name = listofitems[0] + " " + listofitems[1]
        score = float(listofitems[2])

        if name in histogram:
            histogram[name] = histogram[name] + score

        else:
            histogram[name] = score

        line = s.readline()

    s.close()

    histogram = {key: value for key, value in reversed(sorted(histogram.items(), key=lambda item: item[1]))}

    print("\n\nCharacters in file:", histogram)

except:
    print("an Error occured!")

finally:
    s.close()




"""
    ch = s.read(1)
    while ch != '':
        ch = ch.lower()

        if ch in histogram:
            histogram[ch] = int(histogram.get(ch)) + 1
        else:
            histogram[ch] = 1

        ch = s.read(1)
"""
