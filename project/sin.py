import math

def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

DEGREE_TO_RADIANS = math.pi / 180

def sin_angle(angle, n):
    radians = angle * DEGREE_TO_RADIANS

    sin = 0
    for i in range(0, n):
        sign = (-1)**i
        exp = 2 * i + 1
        sin += radians ** exp / factorial(exp) * sign
    return sin


def main():
    n = int(input("No of terms: "))
    angle = int(input("Angle in degrees: "))
    print(f"sin({angle}°)", sin_angle(angle, n))
    return 0


if __name__ == '__main__':
    main()

