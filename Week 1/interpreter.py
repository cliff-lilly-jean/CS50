def main():

    x, y, z = input("Expression: ").split(" ")

    interpret(x,y,z)


def interpret(x,y,z):
    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "/":
            print(x / z)
        case "*":
            print(x * z)


main()