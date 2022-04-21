# QUESTION NO: 11,12
class polygon:
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


class triangle(polygon):
    def findPerimeter(self):
        peri = sum(self._lengthOfSides)
        return peri

    def findArea(self):
        s = self.findPerimeter() / 2
        area = (s * (s - self._lengthOfSides[0]) * (s - self._lengthOfSides[1]) * (s - self._lengthOfSides[2])) ** 0.5
        return area


class eqTriangle(triangle):
    def findPerimeter(self):
        return 3 * self._lengthOfSides[0]

    def __add__(self, tri):
        return self.findPerimeter() + tri.findPerimeter()


p = eqTriangle(3)
q = eqTriangle(3)
p.inputSides()
p.dispSides()
q.inputSides()
q.dispSides()

print(p + q)
