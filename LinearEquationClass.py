class Linear:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    def getDiscriminant(self):
        return (self.__a * self.__d) - (self.__b * self.__c)
    def isSolvable(self):
        if Linear.getDiscriminant(self) != 0:
            return True
    def getX(self):
        if Linear.isSolvable(self):
            return ((self.__e * self.__d) - (self.__b * self.__f)) / self.getDiscriminant()
        else:
            return "The equation has no solution"
    def getY(self):
        if Linear.isSolvable(self):
            return ((self.__a * self.__f) - (self.__e * self.__c)) / self.getDiscriminant()
        else:
            return "The equation has no solution"