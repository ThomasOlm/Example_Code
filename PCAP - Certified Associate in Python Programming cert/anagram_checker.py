##making a program to check if two words are anagrams

def is_anagram(anagram_one, anagram_two):

    anagram_one = anagram_one.lower()
    anagram_two = anagram_two.lower()

    count_one = 0
    count_two = 0

    for char in anagram_one:
        count_one += ord(char)

    for char in anagram_two:
        count_two += ord(char)

    if count_two == count_one:
        print("Anagrams!")
    else:
        print("Nope")

is_anagram("Listen", "Silent")
