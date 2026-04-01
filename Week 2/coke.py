def main():
    amount_for_coke = 50
    change = 50
    amount_due = 0

    while amount_for_coke > 0:
        inserted_coin = int(input("Insert a coin "))

        match inserted_coin:
            case 5:
                change -= 5
                amount_due = change
            case 10:
                change -= 10
                amount_due = change
            case 25:
                change -= 25
                amount_due = change
            case 50:
                change -= 50
                amount_due = change
            case _:
                print("We don't accept those denominations: ")

        amount_for_coke = amount_due

        if amount_due <= 0:
            amount_due = 0

        print(f"Amount due: {amount_due}")

    print(f"Change Owed: {-change}")


main()