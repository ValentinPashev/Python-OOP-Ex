class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class PasswordTooShort(Exception):
    pass


class PasswordMustStartsWithUpper(Exception):
    pass


class PasswordNeedToContainAtLeastOneNumber(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "net", "org")
MIN_COUNT_OF_SYMBOLS = 4

email = input()

while email != "End":

    if len(email.split("@")[0]) <= MIN_COUNT_OF_SYMBOLS:
        raise NameTooShortError("Name must be more than 4 characters")

    if email.count("@") > 1:
        raise MustContainAtSymbolError("Email must contain no more than 1 @!")
    elif email.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")

    if (email.split(".")[-1]) not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print(f"Email is valid")

    email = input()

MIN_COUNT_OF_SYMBOLS_FOR_PASS = 10

password = input()
NUMBERS_FOR_PASSWORD = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
starts_with_upper = True
pass_have_number = False

while password != "End":

    if not password[0].isupper():
        raise PasswordMustStartsWithUpper("Password should start with upper case letter!")

    if len(password) <= 10:
        raise PasswordTooShort("Password must contain at least 10 symbols!")

    if any(char.isdigit() for char in password):
        pass_have_number = True
        print(f"Password is Valid!")
        break

    else:
        raise PasswordNeedToContainAtLeastOneNumber(f"Password needs to contain at least one number")
