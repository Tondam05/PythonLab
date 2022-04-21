# QUESTION NO: 9,10

class Polygon:
    def __init__(self, sides=0):
        self._sides = sides
        self._lengthOfSides = []

    def inputSides(self):
        for i in range(self._sides):
            self._lengthOfSides.append(int(input("Enter length of side: ")))

    def dispSides(self):
        print("Length of sides: ")
        for i in range(self._sides):
            print(self._lengthOfSides[i])


class Triangle(Polygon):
    def findPerimeter(self):
        peri = sum(self._lengthOfSides)
        return peri

    def findArea(self):
        s = self.findPerimeter() / 2
        area = (s * (s - self._lengthOfSides[0]) * (s - self._lengthOfSides[1]) * (s - self._lengthOfSides[2])) ** 0.5
        return area



p = Triangle(3)
p.inputSides()
p.dispSides()
print(p.findPerimeter())
print(p.findArea())