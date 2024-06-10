class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        is_len_valid = len(value) >= 8
        is_upper_valid = len([x for x in value if x.isupper()]) > 0
        is_digit_present = len([x for x in value if x.isdigit()]) > 0

        is_valid = is_upper_valid and is_len_valid and is_digit_present

        if not is_valid:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)