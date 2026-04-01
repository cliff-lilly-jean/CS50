def main():
    hours, minutes = input("What time is it? ").split(":")

    time = hours + minutes

    convert(time)


def convert(time):

    time = int(time)

    if 700 <= time < 800:
        print("Breakfast time")
    elif 1200 <= time < 1300:
        print("Lunch time")
    elif 1800 <= time < 1900:
        print("Dinner time")


if __name__ == "__main__":
    main()