def main():
    start = 10  # Starting number of stones
    remaining = start
    turn = 1

    while remaining > 0:
        print("There are", remaining, "stones left.")
        take = int(input("Player " + str(turn) + ", would you like to remove 1 or 2 stones? "))
        while take < 1 or take > 2:
            take = int(input("Please enter 1 or 2: "))
        remaining -= take
        if remaining == 0:
            print()
            print("Player", 3 - turn, "wins!")
            break
        turn = 2 if turn == 1 else 1
        print()


main()
