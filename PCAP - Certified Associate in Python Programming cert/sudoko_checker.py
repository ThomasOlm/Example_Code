## making a soduko checking program


def sudoko_list(number_set):

    sudoko_set = []
    string_number_set = str(number_set)
    counter = 0
    new_list = []

    # break the raw numbers into a list of 9 lists
    for char in string_number_set:
        if counter <= 8:
            new_list.append(int(char))

        if counter == 9:
            sudoko_set.append(new_list)
            counter = 0
            new_list = []
            new_list.append(int(char))

        counter += 1
    else:
       sudoko_set.append(new_list)


    #now we have to do three separate checks, row, column, and sub-square
    #
    #ROW CHECK: sum the list to check if it is equal to 45

    row_check = 0
    for row in sudoko_set:
        if sum(row) == 45:
            row_check += 1

    if row_check == 9:

        row_check = 1
    else:
        row_check = 0

    #COLUMN CHECK: sum the first digit of every list within sudoko_list
    column_sum = 0
    column_check = 0

    for x in range(len(sudoko_set)):
        column_sum = 0
        for y in range(len(sudoko_set)):
            column_sum += sudoko_set[y][x]

        if column_sum == 45:
           column_check += 1

    if column_check == 9:
        column_check = 1

    else:
        column_check = 0

    ## SUBSQUARE CHECK

    sub_one = 0
    sub_two = 0
    sub_three = 0
    subsquare_check = 0

    for row in range(len(sudoko_set)):

        for column in range(len(sudoko_set)):

            if column < 3:
                sub_one += sudoko_set[row][column]

            elif column >= 3 and column < 6:
                sub_two += sudoko_set[row][column]

            elif column >= 6:
                sub_three += sudoko_set[row][column]

        if sub_one == 45 and sub_two == 45 and sub_three == 45:
            subsquare_check += 3

        if row == 2 or row == 5 or row == 8:
           sub_one = 0
           sub_two = 0
           sub_three = 0

    if subsquare_check == 9:
        subsquare_check = 1

    else:
        subsquare_check = 0

    ## FINAL CHECK

    if row_check == 1 and column_check == 1 and subsquare_check == 1:
        return True
    else:
        return False
        
sudoko_num = 295743861431865927876192543387459216612387495549216738763524189928671354154938672

            #295743861
            #431865927
            #876192543
            #387459216
            #612387495
            #549216738
            #763524189
            #928671354
            #154938672
            
print(sudoko_list(sudoko_num))
#output is True
print(sudoko_list(195743862431865927876192543387459216612387495549216738763524189928671354254938671))
#Output is False 
