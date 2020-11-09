#Create class
class User:
    #Constructor
    def __init__(self, age, name, proffesion):
        self.age = age
        self.name = name
        self.proffesion = proffesion

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_brithday(self):
        self.age += 1

#customer class
class Customer(User):
    def __init__(self, age, name, proffesion, balance):
        self.age = age
        self.name = name
        self.proffesion = proffesion
        self.balance = balance
    
    def set_balance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"


#Init user object

astra = User(17, 'Velocity', 'coding')
lone = User(12, 'kia', 'gaming')

#Edit property
astra.age = 18

astra.has_brithday()


#call method
print(astra.greeting())

tarun = Customer(10, 'Tarun Sharma', 'web', 500)
tarun.set_balance(50)
print(tarun.greeting())

# print(astra.age)
# print(lone.name)
