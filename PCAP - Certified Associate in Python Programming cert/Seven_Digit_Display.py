#this is a program to display an inputed number in made up of seven hashes
def seven_seg(number):
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    fifth_line = ""

    for char in number:

        if int(char) == 1:

            first_line +=  "#"
            second_line += "#"
            third_line +=  "#"
            fourth_line += "#"
            fifth_line +=  "#"

        elif int(char) == 2:

            first_line +=  "###"
            second_line += "  #"
            third_line +=  "###"
            fourth_line += "#  "
            fifth_line +=  "###"

        elif int(char) == 3:

            first_line +=  "###"
            second_line += "  #"
            third_line +=  "###"
            fourth_line += "  #"
            fifth_line += "###"

        elif int(char) == 4:

            first_line +=  "# #"
            second_line += "# #"
            third_line +=  "###"
            fourth_line += "  #"
            fifth_line +=  "  #"

        elif int(char) == 5:

            first_line +=  "###"
            second_line += "#  "
            third_line +=  "###"
            fourth_line += "  #"
            fifth_line +=  "###"

        elif int(char) == 6:

            first_line +=   "###"
            second_line +=  "#  "
            third_line +=   "###"
            fourth_line +=  "# #"
            fifth_line +=  "###"

        elif int(char) == 7:

            first_line +=  "###"
            second_line += "  #"
            third_line +=  "  #"
            fourth_line += "  #"
            fifth_line +=  "  #"

        elif int(char) == 8:

            first_line +=  "###"
            second_line += "# #"
            third_line +=  "###"
            fourth_line += "# #"
            fifth_line +=  "###"

        elif int(char) == 9:

            first_line +=  "###"
            second_line += "# #"
            third_line +=  "###"
            fourth_line += "  #"
            fifth_line +=  "  #"

        elif int(char) == 0:

            first_line +=  "###"
            second_line += "# #"
            third_line +=  "# #"
            fourth_line += "# #"
            fifth_line +=  "###"

        else:
            return "invalid input!"

        first_line += " "
        second_line += " "
        third_line += " "
        fourth_line += " "
        fifth_line += " "




    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)

number = input("Please enter a number: ")
seven_seg(number)
