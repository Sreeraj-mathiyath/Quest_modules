# class BankAccount:
#     bank_name = "Safe Bank"      

#     def __init__(self, account_no, balance):
#         self._account_no = account_no   # Protected: accessible in class and subclasses
#         self.__balance = balance        # Private: accessible only inside class

#     # Public method
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     # Public method
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn ₹{amount}. New balance: ₹{self.__balance}")
#         else:
#             print("Insufficient balance.")

#     # Public method to access private variable
#     def get_balance(self):
#         return self.__balance


# class Branch(BankAccount):
#     def __init__(self, account_no, balance):
#         super().__init__(account_no, balance)



# calicut = Branch(101,700)
# calicut.get_balance()
# print(calicut._account_no)
# print(calicut.__balance)




from abc import ABC,abstractmethod
 
 
class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def EnterPin(self):
        pass

    def deposit(self):
        pass


class NewVersionATM(ATM):

    def withdraw(self):
        print('you can withdraw cash')

    def EnterPin(self):
        print('You can enter pin')

    def PinGeneration(self):
        print('you can generate new pin with this ATM')

a = NewVersionATM()