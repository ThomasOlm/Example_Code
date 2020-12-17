## making a program to find the if the characters of one string are in another

def find_the_string(string_one, string_two):

    list_one = []

    for char in string_one:
        list_one.append(char)

    print(list_one)
    counter = 0

    for char in list_one:
        if char in string_two:
            counter += 1

    if counter == len(string_one):
        print("yes")
    else:
        print("NO")


find_the_string("donut", "Nabucodonosor")
# output is "NO"

find_the_string("donor", "Nabucodonosor")
# output is "yes"
