import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

math = None
operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
if operation == '1':
    num1 = int(input("Podaj składnik 1. "))
    num2 = int(input("Podaj składnik 2. "))
    print(f"Dodaję {num1} i {num2}")
    math = (num1 + num2)
elif operation == '2':
    num1 = int(input("Podaj składnik 1. "))
    num2 = int(input("Podaj składnik 2. "))
    print(f"Odejmuję {num1} i {num2}")
    math = (num1 - num2)
elif operation == '3':
    num1 = int(input("Podaj składnik 1. "))
    num2 = int(input("Podaj składnik 2. "))
    print(f"Mnożę {num1} i {num2}")
    math = (num1 * num2)
elif operation == '4':
    num1 = int(input("Podaj składnik 1. "))
    num2 = int(input("Podaj składnik 2. "))
    print(f"Dzielę {num1} i {num2}")
    math = (num1 / num2)
    if num2 == 0:
        print("Nie dzielimy przez zero!")
        exit(1)
else:
    print("Proszę wprowadzać liczby od 1 do 4")
    exit(1)

if __name__ == "__main__":
    logging.debug("The program was called with this parameter %s" % operation)
    logging.debug("First parameter is %s" % num1)
    logging.debug("Second parameter is %s" % num2)

print("Wynik to %s" % math)