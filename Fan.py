class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, on=False, radius=5, color='blue'):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def getSpeed(self):
        return self.__speed
    def getOn(self):
        return self.__on
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def setFanOn(self):
        self.__on = True
    def setFanOff(self):
        self.__on = False
    def setSpeedSlow(self):
        self.__speed = self.slow
        return self.__speed
    def setSpeedMedium(self):
        self.__speed = self.medium
        return self.__speed
    def setSpeedFast(self):
        self.__speed = self.fast
        return self.__speed
    def setColor(self,color):
        self.__color = color
    def setRadius(self, radius):
        self.__radius = radius

