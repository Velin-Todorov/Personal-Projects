from fractions import Fraction


def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponential")


def add():
    a = Fraction(input("Please enter a fraction: "))
    b = Fraction(input("Please enter a fraction: "))
    return a + b


def subtract():
    a = Fraction(input("Please enter a fraction: "))
    b = Fraction(input("Please enter a fraction: "))
    return a - b


def multiply():
    a = Fraction(input("Please enter a fraction: "))
    b = Fraction(input("Please enter a fraction: "))
    return a * b


def division():
    a = Fraction(input("Please enter a fraction: "))
    b = Fraction(input("Please enter a fraction: "))
    return a / b


def exponential():
    a = Fraction(input("Please enter a fraction: "))
    b = Fraction(input("Please enter a fraction: "))
    return a ** b


if __name__ == '__main__':
    try:
        while True:
            menu()
            choice = input("Please enter make a choice: ")

            if choice == '1':
                print(f'The result is: {add()}')
                a = input('Would you like to try again? Y(yes), N(no)')

                if a == 'Y':
                    continue
                else:
                    print('Thank you.')
                    break

            elif choice == '2':
                print(f'The result is: {subtract()}')
                a = input('Would you like to try again? Y(yes), N(no)')

                if a == 'Y':
                    continue
                else:
                    print('Thank you.')
                    break

            elif choice == '3':
                print(f'The result is: {multiply()}')
                a = input('Would you like to try again? Y(yes), N(no)')

                if a == 'Y':
                    continue
                else:
                    print('Thank you.')
                    break

            elif choice == '4':
                print(f'The result is: {division()}')
                a = input('Would you like to try again? Y(yes), N(no)')

                if a == 'Y':
                    continue
                else:
                    print('Thank you.')
                    break

            elif choice == '5':
                print(f'The result is: {exponential()}')
                a = input('Would you like to try again? Y(yes), N(no)')

                if a == 'Y':
                    continue
                else:
                    print('Thank you.')
                    break

    except ZeroDivisionError as z:
        print(z)
        print("Please launch the program again")
