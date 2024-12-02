def count_characters():
    n = input("Enter a string: ")
    newlist = [i for i in n.casefold()]
    dict = {}.fromkeys(newlist, 0)

    for i in newlist:
        if i in dict:
            dict[i] += 1

    print("\nCharacter Frequency Count:")
    print(n)
    print(dict)

def add_ing_or_ly():
    n = input("\nEnter a string to add 'ing' or 'ly': ")

    if len(n) >= 3:
        if n[-3:] != "ing":
            print(n + "ing")
        else:
            print(n + "ly")
    else:
        print(n)

def longest_word_length():
    list_of_words = ["Hello", "World", "programming", "python", "Advanced DS"]
    print("\nWords List:")
    print(list_of_words)

    a = 0

    for i in list_of_words:
        if len(i) > a:
            a = len(i)

    print(f"The length of the longest word is: {a}")

def print_star_patterns():
    n = 5

    print("\nIncreasing Star Pattern:")
    for i in range(n):
        for j in range(i):
            print('* ', end="")
        print('')

    print("\nDecreasing Star Pattern:")
    for i in range(n, 0, -1):
        for j in range(i):
            print('* ', end="")
        print('')

def main():
    count_characters()
    add_ing_or_ly()
    longest_word_length()
    print_star_patterns()

if __name__ == "__main__":
    main()
