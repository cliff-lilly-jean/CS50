def main():
    use_indoor_voice()


def use_indoor_voice():
    user_voice = input("Type what you want to say: ")
    user_voice = user_voice.lower()
    print(f"You said: {user_voice}")

main()