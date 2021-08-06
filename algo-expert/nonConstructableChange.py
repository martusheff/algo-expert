
coins = [109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]

def main(coins):
    coins.sort()
    current_amount = 1
    coins_checked = 1
    checking = True
    reached = 0

    if coins != []:

        while checking:

            for i in range(coins_checked):
                reached += coins[i]
                if reached == current_amount:
                    current_amount += 1
                    reached = 0
                else:
                    checking = False
                    return current_amount

        print(current_amount)
    else:

        return 1

if __name__ == '__main__':
    main(coins)