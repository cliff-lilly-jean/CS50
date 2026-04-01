def main():
    user_input = input("Add a camel case word ")

    result = ""

    for letter in user_input:
        if letter.isupper():
            result += "_" + letter.lower()
        else:
            result += letter

    print(result)


main()