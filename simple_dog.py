class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        print(f"{self.name} is rolling")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 4)
print(f"My dog name's {my_dog.name}")
print(f"My dog is {your_dog.age} years old!")
my_dog.sit()
your_dog.sit()
