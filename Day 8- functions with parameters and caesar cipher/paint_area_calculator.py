import math
def paint_calc(height, width, cover):
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    number_of_cans =(test_h * test_w) / coverage
    print("You'll need" + " " + str(math.ceil(number_of_cans)) + " " + "cans of paint")

paint_calc(height="test_h", width="test_w", cover="coverage")
