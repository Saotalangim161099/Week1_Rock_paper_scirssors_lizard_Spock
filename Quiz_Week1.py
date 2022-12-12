# practice Quiz 1 questions
import math


# practice Math method
def f(x):
    return ((-5 * math.pow(x, 5)) + (69 * math.pow(x, 2)) - 47)


def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value * math.pow(1 + rate_per_period, periods)


def area_regular_polygon(no_of_sides, length_of_each_side):
    a = math.tan(math.pi / no_of_sides)
    b = (no_of_sides) * math.pow(length_of_each_side, 2)
    c = b / a
    return c / 4


def max_of_2(a, b):
    if (a > b):
        return a
    else:
        return b


def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))


def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print(point_x * scale, point_y * scale)


if __name__ == '__main__':
    # first part
    n = 123
    print((int)((n % 100 - n % 10) / 10))  # convert the result from float to integer
    # print("n - n % 10:",(n - n % 10))
    # print(((n - n % 10) / 10) % 10)
    # print((n - n % 10) / 10)
    # print("f(0): " + str((int)(f(0))))
    # print("f(1): " + str((int)(f(1))))
    # print("f(2): " + str((int)(f(2))))
    # print("f(3): " + str((int)(f(3))))
    # print("$500 at 4% compounded daily for 10 years yield $", future_value(500, 0.04, 10, 10))
    # print("$1000 at 2% compounded daily for 3 years yield $", future_value(1000, 0.02, 365, 3))
    print(area_regular_polygon(5, 7))
    print(area_regular_polygon(7, 3))
