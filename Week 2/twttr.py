def main():
    user_input = input("Input ")
    word_list = []
    vowels_list = ["a", "e", "i", "o", "u"]

    for letter in user_input:

        word_list.append(letter)
        if letter.lower() in vowels_list:
            word_list.pop()

    converted_word = "".join(word_list)

    print(converted_word)

main()