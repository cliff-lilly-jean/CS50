def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: length must be between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: first two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Rule 3: all characters must be alphanumeric
    for char in s:
        if not char.isalnum():
            return False

    # Rule 4: numbers must be at the end, and first number can't be 0
    for i in range(len(s)):
        if s[i].isdigit():
            # first number cannot be 0
            if s[i] == "0":
                return False

            # everything after first number must also be digits
            for char in s[i:]:
                if not char.isdigit():
                    return False
            break

    return True


main()