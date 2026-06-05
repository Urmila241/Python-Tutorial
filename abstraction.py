# from abc import ABC, abstractmethod
# class A(ABC):
#     @abstractmethod
#     def anyMethod(self):
#         pass
# class B(A):
#         def anyMethod(self):
#                print("hello from anymethod")


#         def myMethod(self):
#             print("Hello from MyMethod")  
# obj=B() 
# obj.myMethod()
# obj.anyMethod()


# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     def __init__(self,brand,type):
#           self.brand=brand
#           self.type=type
#     @abstractmethod
#     def startengine(self):
#         pass
#     def showInfo(self):
#          print(f"brand = {self.brand} and type = {self.type}")
# class Car(Vehicle):
#      def startengine(self):
#           print("car starts")
#      def maxspeed(self):
#         print("max speed is 180km/min")
# class Bike(Vehicle):
#      def startengine(self):
#           print("bike starts")
#           def maxspeed(self):
#                print("max speed is 80km/min")
# obj=Car("swift","Auto")
# obj.showInfo()
# obj.startengine
# obj.maxspeed()

from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self,Username,pasward,balance):
        self.Username=Username
        self.pasward=pasward
        self.balance=balance
    @abstractmethod
    def withdraw(amount):
        pass
    @abstractmethod
    def deposit(self,amount):
        pass
class Current(Bank):
     def withdraw(self, amount):
         user_name=input("Enter Name:")
         user_passward=input("Enter passward:")
         if amount<=self.balance:
          self.balance-=amount
          print(f"{amount}withdraw successfully.")
          print(f"Remaining balance:{self.balance}")
         else:
            print("Insufficient balance!")
     def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited successfully.")
            print(f"Updated balance:{self.balance}")
        else:
            print("Invalid deposit amount!")
class Saving(Bank):
    def withdraw(self,amount):
        user_name=input("Enter Name:")
        user_passward=input("Enter passward:")
        if amount<self.balance:
            self.balance-=amount
            print(f"{amount} withdraw successfully.")
            print(f"Remaining balance:{self.balance}")
        else:
            print("Cannot withdraw.")
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited successfully.")
            print(f"Updated balance: {self.balance}")
        else:
            print("Invalid deposit amount!")
c1=Current("Urmila", "1234", 1000)
s1=Saving("Sapna", "5678", 500)
print("Current Account")
c1.deposit(2000)
c1.withdraw(3000)
print("Saving Account")
s1.deposit(500)
s1.withdraw(500)