## making a palindrome testing function

def is_palindrome(palindrome):
    palindrome = palindrome.lower()
    palindrome_list_one = []

    for char in palindrome:
        palindrome_list_one.insert(0, char)


    list_char = ''.join(palindrome_list_one)

    if list_char.replace(" ", "") == palindrome.replace(" ", ""):
        print("Palindrome!")
    else:
        print("Not a palindrome")

is_palindrome("ten animals i slam in a net")
