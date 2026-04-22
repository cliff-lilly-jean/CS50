def main():

    import sys

    # check for 1 command line argument, else sys.exit()
    if sys.argv[2:]:
        print("too many arguments")
        sys.exit()
    else:
        print("good")

    # check the file exists, else sys.exit()

    # check the file ends in .py, else sys.exit()
    if sys.argv[1].endswith(".py"):
        print("Correct format")
    else:
        sys.exit()




    # check for #,  skip
    # check for whitespace, skip







main()