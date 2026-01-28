# from abc import ABC,abstractmethod


# class Polygen(ABC):
#     def hello(self):
#         print('helllooo')

#     @abstractmethod
#     def Area(self):
#         print('areaaaaaaaaaaaaaa')    


# class Rectangle(Polygen):
#     def Perimeter(self):
#         print('rectanle"s perimeter ')
#     def Area(self):
#         print('rect area')
#         super().Area()

# book=Rectangle()
# book.Perimeter()
# book.Area()



class Humen:
    def walk(self):
        print('walking')
    
    def running(self):
        print("Running..........")


class Student(Humen):
    def study(self):
        self.walk()
        super().walk()
        print('can study')
    
    def walk(self):
        self.running()
        super().running()
        print("Walking in the moon light..........")

    def running(self):
        print("Running..................................")



anu=Student()
anu.walk()