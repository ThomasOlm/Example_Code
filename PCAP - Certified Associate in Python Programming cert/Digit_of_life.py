##making a program to return a "digit of life"

def digit_of_life(birth):
    count = 0
    list_of_birth = [int(x) for x in str(birth)]


    for num in list_of_birth:
        count += num

    if count > 10:
        digit_of_life(count)
    else:
        return count


print(digit_of_life(20000101))
