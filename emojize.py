def main():
    # import the libraries
    import emoji
    import sys

    # get the the users text string
    user_str = input("Input ")

    # determine if the text string is a valid emoji, if it isn't send a message and rerun to get the users text string
    print(emoji.emojize(user_str, language="alias"))




main()