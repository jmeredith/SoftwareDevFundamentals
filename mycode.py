#! /usr/bin/python
class Vehicle(object):
    def __init__(self, wheels):
        self.NumWheels = wheels

    def GetWheels(self):
        return self.NumWheels

class Car(Vehicle):
    def __init__(self, color, wheels = 4):
        self.NumWheels = wheels
        self.CarColor = color

    def GetColor(self):
        return self.CarColor

mustang = Car("yellow")
lorry = Vehicle("8")
print ( mustang.GetColor())
print ( mustang.GetWheels())
print ( lorry.GetWheels())

