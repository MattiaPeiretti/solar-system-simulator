import math
import costants


def g_force_x(x1, x2, y1, y2, m):
    Fx = 0
    Fy = 0

    Ax = accelleration(x1, )
    Ay = accelleration()


def calculate_gravitational_accelleration(mass, radius):
    return (costants.GRAVITATIONAL_COSTANT * mass) / (radius**2)


def accelleration(x1, x2, y1, y2, g):

    deltaX = x1 - x2
    deltaY = y1 - y2

    # if (x1 >= x2):
    #     deltaX = x1 - x2
    # else:
    #     deltaX = x2 - x1

    # if (y1 >= y2):
    #     deltaY = y1 - y2
    # else:
    #     deltaY = y2 - y1

    if (deltaX < 0):
        signX = -1
    else:
        signX = 1

    if (deltaY < 0):
        signY = -1
    else:
        signY = 1

    abs_distanceX = distance(x1, x2, y1, y2) * signX
    abs_distanceY = distance(x1, x2, y1, y2) * signY
    angle1 = math.asin(deltaX / abs_distanceX)
    angle2 = math.asin(deltaY / abs_distanceY)
    force = g

    return ((force * math.sin(angle1)) * signX, (force * math.sin(angle2)) * signY)

# def accelleration(x1, x2, y1, y2, g):
#     deltaX = x2 - x1
#     deltaY = y2 - y1
#     if (deltaX < 0):
#         sign = -1
#     else:
#         sign = 1

#     abs_distance = distance(x1, x2, y1, y2) * sign
#     angle1 = math.asin(deltaX / abs_distance)
#     angle2 = math.asin(deltaY / abs_distance)
#     force = g / math.pow(abs_distance, 2)

#     return ((force * math.sin(angle1)) * sign, (force * math.sin(angle2)) * sign)


def distance(x1, x2, y1, y2):
    return math.hypot(x2-x1, y2-y1)
