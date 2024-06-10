import tkinter as tk


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
MIN_COUNT_OF_SYMBOLS_FOR_PASS = 10


def validate_email():
    email = entry_email.get()

    try:
        if len(email.split("@")[0]) <= MIN_COUNT_OF_SYMBOLS:
            raise NameTooShortError("Name must be more than 4 characters")

        if email.count("@") > 1 or email.count("@") < 1:
            raise MustContainAtSymbolError("Email must contain exactly 1 @ symbol")

        if (email.split(".")[-1]) not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        result_label.config(text="Email is valid")
    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as e:
        result_label.config(text=str(e))


def validate_password():
    password = entry_password.get()

    try:
        if not password[0].isupper():
            raise PasswordMustStartsWithUpper("Password should start with an uppercase letter")

        if len(password) <= MIN_COUNT_OF_SYMBOLS_FOR_PASS:
            raise PasswordTooShort("Password must contain at least 10 symbols")

        if not any(char.isdigit() for char in password):
            raise PasswordNeedToContainAtLeastOneNumber("Password needs to contain at least one number")

        result_label_password.config(text="Password is valid")
    except (PasswordMustStartsWithUpper, PasswordTooShort, PasswordNeedToContainAtLeastOneNumber) as e:
        result_label_password.config(text=str(e))


window = tk.Tk()
window.title("Email and Password Validator")
window.geometry("400x300")

label_email = tk.Label(window, text="Enter your email:")
label_email.pack()

entry_email = tk.Entry(window, width=30)
entry_email.pack()

button_validate_email = tk.Button(window, text="Validate Email", command=validate_email)
button_validate_email.pack()

result_label = tk.Label(window, text="")
result_label.pack()

label_password = tk.Label(window, text="Enter your password:")
label_password.pack()

entry_password = tk.Entry(window, show="*", width=30)
entry_password.pack()

button_validate_password = tk.Button(window, text="Validate Password", command=validate_password)
button_validate_password.pack()

result_label_password = tk.Label(window, text="")
result_label_password.pack()

window.mainloop()
