def main():
    slow_down_playback()

def slow_down_playback():
    user_input = input("What would you like to say? ")
    print(user_input.replace(" ", "..."))



main()