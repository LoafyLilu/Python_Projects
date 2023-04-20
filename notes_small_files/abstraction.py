#importing abstract base classes and methods
from abc import ABC, abstractmethod

#creating class from abc
class Canvas(ABC):
    #regular method
    def purpose(self):
        print("As an artist, your purpose can be")
    @abstractmethod
    #creating abstract method and leaving the function blank
    def create(self):
        pass

#creating child classes from abstract class Canvas
class Sketchbook(Canvas):
    def create(self):
        print("Sketching with pen and paper!\n")

class Tablet(Canvas):
    def create(self):
        print("Creating digital artwork!\n")

#creating objects of each child class and passing in the abstract and regular methods
obj = Sketchbook()
obj.purpose()
obj.create()

obj2 = Tablet()
obj2.purpose()
obj2.create()


        
