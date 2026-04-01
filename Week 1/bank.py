def main():
    payment()

def payment():
    user_response = input("Greeting: ").lower()

    if "hello" in user_response:
        print("$0")
    elif user_response.startswith("h"):
        print("$20")
    else:
        print("$100")


main()