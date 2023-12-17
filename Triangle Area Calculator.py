import math

def isValid(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

def area(side1, side2, side3):
    if isValid(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
        return area
    else:
        return None

def main():
    count = 0
    while count < 2:
        side1 = float(input("Enter the first side: "))
        side2 = float(input("Enter the second side: "))
        side3 = float(input("Enter the third side: "))

        if isValid(side1, side2, side3):
            triangle_area = area(side1, side2, side3)
            if triangle_area is not None:
                print(f"The area of the triangle is {triangle_area:.16f}")
            else:
                print("Input is invalid")
        else:
            print("Input is invalid")

        count += 1

if __name__ == "__main__":
    main()