# ----------------------------------------------------------------------
# Name:     Homework 2
# Purpose:  Implement a cash register
#
# Author:   Ian Soohoo and Trieu Nguyen
# ----------------------------------------------------------------------
""" Cash Register

User enters total amount due and cash tendered. Cash register prints
the total change in $ and splits the due cash in twenties, tens, fives,
ones, and quarters, dimes, nickels, and pennies.
"""



import math


def change_calculator():
    """
    Calculate change

    Prompt the user to enter the total due (maximum amount is 999)
    and tender.
    Calculate change by letting tender subtracts total.

    Returns:
        float: the result of subtraction between tender and total amount
    """
    in_range = False  # true if entered amount in the range of 0 to 999
    while in_range is False:
        # Prompt user to enter the total due amount
        total = float(input('Please enter the total amount due in $'))
        if (0 < total < 999):
            in_range = True

    enough = False  # true if tender is at least equal to total due
    while enough is False:
        # Prompt user to enter tender
        tender = float(input('Please enter the cash tendered in $'))
        if (tender >= total):
            enough = True
        print(f'The cash tendered must be at least $, {total:.2f}')

    change = tender - total  # calculate change

    print(f'{"Total Amount: ":<15} $ {total: >6.2f}')
    print(f'{"Cash tendered: ":<15} $ {tender: >6.2f}')
    print(f'{"Change Due: ":<15} $ {change: >6.2f}')

    return change


def change_distribution(change_amount):
    """Calculate cash change distribution

    Compute the number of $20, $10, $5 and $1 bills and the number of
    quarters, dimes, nickels and pennies due.

    Parameters:
        change_amount (float): the amount of change

    Returns:
        Array of change distribution of $20 (at index 0 of the array),
        $10 (index 1), $5 (index 2), $1 bills (index 3) and the number
        of quarters (index 4), dimes (index 5), nickels (index 6)
        and pennies (index 7).
    """

    leftover_change = change_amount  # keeps track of the leftover
    changes = [0, 0, 0, 0, 0, 0, 0, 0]  # store change distribution

    # check if the change amount is bigger or equal to 20
    if (leftover_change >= 20):
        # calculate and store the number of $20 bills
        changes[0] = int(leftover_change / 20)
        # calculate the leftover change
        leftover_change = leftover_change % 20

    # check if the change amount is bigger or equal to 10
    if (leftover_change >= 10):
        # calculate and store the number of $10 bills
        changes[1] = int(leftover_change / 10)
        # calculate the leftover change
        leftover_change = leftover_change % 10

    if (leftover_change >= 5):
        changes[2] = int(leftover_change / 5)
        leftover_change = leftover_change % 5

    if (leftover_change >= 1):
        changes[3] = int(leftover_change / 1)
        leftover_change = leftover_change - changes[3]

    if (leftover_change >= 0.25):
        changes[4] = int(leftover_change / 0.25)
        leftover_change = leftover_change % 0.25

    if (leftover_change >= 0.1):
        changes[5] = int(leftover_change / 0.1)
        leftover_change = leftover_change % 0.1

    if (leftover_change >= 0.05):
        changes[6] = int(leftover_change / 0.05)
        leftover_change = leftover_change % 0.05

    if (leftover_change > 0):
        # calculate and store the number of pennies
        # and also take care of float property
        changes[7] = int(math.ceil((leftover_change / 0.01) * 100)/100)

    return changes


def print_result(twenty_bills, ten_bills, five_bills, one_bills,
                 quarters, dimes, nickles, pennies):
    """Print result of change distribution

    Print the number of $20, $10, $5 and $1 bills and the number of
    quarters, dimes, nickels and pennies due.

     Parameters:
        twenty_bills (int): number of twenty bills
        ten_bills (int): number of ten bills
        five_bills (int): number of five bills
        one_bills (int): number of one bills
        quarters (int): number of quarters
        dimes (int): number of dimes
        nickles (int): number of nickles
        pennies (int): number of pennies

    """
    if (twenty_bills > 1):
        print(f'{twenty_bills:<2} $20 bills')
    elif (twenty_bills is 1):
        print("1  $20 bill")
    else:
        pass

    if (ten_bills > 1):
        print(f'{ten_bills:<2} $10 bills')
    elif (ten_bills is 1):
        print("1  $10 bill")
    else:
        pass

    if (five_bills > 1):
        print(f'{five_bills:<2} $5 bills')
    elif (five_bills is 1):
        print("1  $5 bill")
    else:
        pass

    if (one_bills > 1):
        print(f'{one_bills:<2} $1 bills')
    elif (one_bills is 1):
        print("1  $1 bill")
    else:
        pass

    if (quarters > 1):
        print(f'{quarters:<2} quarters')
    elif (quarters is 1):
        print("1  quarter")
    else:
        pass

    if (dimes > 1):
        print(f'{dimes:<2} dimes')
    elif (dimes is 1):
        print("1  dime")
    else:
        pass

    if (nickles > 1):
        print(f'{nickles:<2} nickles')
    elif (nickles is 1):
        print("1  nickle")
    else:
        pass

    if (pennies > 1):
        print(f'{pennies:<2} pennies')
    elif (pennies is 1):
        print("1  penny")
    else:
        pass


def main():
    change_amount = change_calculator()
    distribution = change_distribution(change_amount)
    print_result(distribution[0], distribution[1], distribution[2],
                 distribution[3], distribution[4], distribution[5],
                 distribution[6], distribution[7])


if __name__ == "__main__":
    main()


