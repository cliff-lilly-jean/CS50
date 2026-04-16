def main():

    import inflect

    names = []
    sentence = inflect.engine()

    try:
        while True:
            line = input("Name: ")
            names.append(line)
    except EOFError:
        sentence.join(names)
        print(f"\n Adieu, adieu, to {sentence.join(names)}")



main()