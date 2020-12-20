## practicing with try and exception blocks

def read_int(prompt, min, max):
    print(prompt)

    try:
        num = int(input("Enter num now: "))
        try:

            if num >= min and num <= max:
                return num

            else:
                raise IndexError

        except IndexError:
            print("Error the value is not within the permitted range", min, max)

    except TypeError:
        print("Error Wrong Input!")



v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
