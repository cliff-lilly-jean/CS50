def main():
    great_question_answer()


def great_question_answer():
    answer = input('What is the Answer to the Great Question of Life, the Universe and Everything ').lower()

    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()