import math

class TriangleSolver:
    def __init__(self):
        self.sideA = 0
        self.sideB = 0
        self.sideC = 0
        self.angleA = 0
        self.angleB = 0
        self.angleC = 0

    def solve_sides(self):
        if self.sideA > 0 and self.sideB > 0 and self.angleC > 0:
            self.sideC = self.sideA * math.sin(math.radians(self.angleC)) / math.sin(math.radians(self.angleA))
        elif self.sideA > 0 and self.sideC > 0 and self.angleB > 0:
            self.sideB = self.sideA * math.sin(math.radians(self.angleB)) / math.sin(math.radians(self.angleA))
        elif self.sideB > 0 and self.sideC > 0 and self.angleA > 0:
            self.sideA = self.sideB * math.sin(math.radians(self.angleA)) / math.sin(math.radians(self.angleB))
        else:
            print("Insufficient information to solve for sides.")

    def solve_angles(self):
        if self.angleA > 0 and self.angleB > 0 and self.sideC > 0:
            self.angleC = math.degrees(math.asin(math.sin(math.radians(self.angleA)) * self.sideC / self.sideA))
        elif self.angleA > 0 and self.angleC > 0 and self.sideB > 0:
            self.angleB = math.degrees(math.asin(math.sin(math.radians(self.angleA)) * self.sideB / self.sideA))
        elif self.angleB > 0 and self.angleC > 0 and self.sideA > 0:
            self.angleA = math.degrees(math.asin(math.sin(math.radians(self.angleB)) * self.sideA / self.sideB))
        else:
            print("Insufficient information to solve for angles.")

triangle = TriangleSolver()

print("Enter known values for the triangle (side lengths and angles in degrees):")
triangle.sideA = float(input("Side A: "))
triangle.sideB = float(input("Side B: "))
triangle.sideC = float(input("Side C: "))
triangle.angleA = float(input("Angle A: "))
triangle.angleB = float(input("Angle B: "))
triangle.angleC = float(input("Angle C: "))

triangle.solve_sides()
triangle.solve_angles()

print("Solved Triangle:")
print(f"Side A: {triangle.sideA}")
print(f"Side B: {triangle.sideB}")
print(f"Side C: {triangle.sideC}")
print(f"Angle A: {triangle.angleA} degrees")
print(f"Angle B: {triangle.angleB} degrees")
print(f"Angle C: {triangle.angleC} degrees")
