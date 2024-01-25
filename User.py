class Privileges:

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        print(self.privileges)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} \n Last_name: {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def reading_attempts(self):
        print(f"You have {self.login_attempts} attempts")

class Admin(User):
    
    def __init__(self):
        self.privileges = Privileges() 



permission = Admin()
permission.privileges.show_privileges()

aidar = User("Aidar", "Asankadyrov")
greet = User("Aidar", "Asankadyrov")

greet.greet_user()
aidar.describe_user()
aidar.login_attempts = 2
aidar.increment_login_attempts()
aidar.reading_attempts()

aidar.reset_login_attempts()
aidar.reading_attempts()

