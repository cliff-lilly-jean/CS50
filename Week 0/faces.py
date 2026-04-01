def main():
    user_input = input("create a string: ")
    print(convert(user_input))

def convert(user_string):

    return user_string.replace(":)", "🙂").replace(":(", "🙁")

main()