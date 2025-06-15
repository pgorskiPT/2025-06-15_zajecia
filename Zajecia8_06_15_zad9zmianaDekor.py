# napisać dekorator, który zmieni wynik działania funkcji na duże litery
# zad 12 z zajec 5
from colorama import Fore, Style, init

# pip install colorama

init(autoreset=True)


def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper  # adres funkcji


# bold_decorator \033[1m , \033[0m
def bold_decorator(func):
    def wrapper():
        result = func()
        # return f"\033[1m" + result + "\033[0m"
        return Style.BRIGHT + result    #tu zamiast krzaczków dodalismy dekorator

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!"


# kolejność ma znaczenie
@bold_decorator
@uppercase_decorator
def greeting2():
    return "Hello World!"


print(greeting())  # Hello World! bez dekoratora
# po uzyciu dekoratora uppercase: HELLO WORLD!
print(greeting2())
