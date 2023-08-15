"""

Unit converter
"""
from fractions import Fraction


def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilos to Pounds")
    print("4. Pounds to Kilos")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius ")


def km_miles():
    km = float(input("Enter distance in km: "))
    miles = km / 1.609
    return miles


def miles_km():
    miles = float(input("Enter distance in km: "))
    km = miles * 1.609
    return km


def kg_pounds():
    kg = float(input("Please enter mass in kg: "))
    pounds = kg * 2.205
    return pounds


def pounds_kg():
    pounds = float(input("Please enter the mass in pounds: "))
    kg = pounds / 2.205
    return kg


def celsius_fahr():
    celsius = float(input("Please enter the temperature in Celcius: "))
    fahr = (celsius * Fraction(9, 5)) + 32
    return fahr


def fahr_celsius():
    fahr = float(input("Please enter the temperature in Fahr: "))
    celsius = (fahr - 32) * Fraction(5, 9)
    return celsius


if __name__ == '__main__':
    try:
        print_menu()
        choice = input("Which conversion would you like to do?: ")
        if choice == '1':
            print(km_miles())
        elif choice == '2':
            print(miles_km())
        elif choice == '3':
            print(kg_pounds())
        elif choice == '4':
            print(pounds_kg())
        elif choice == '5':
            print(celsius_fahr())
        elif choice == '6':
            print(fahr_celsius())
        else:
            print('Invalid input')

    except ValueError as e:
        print(e)
        print('Please provide a valid input and start the program again')
