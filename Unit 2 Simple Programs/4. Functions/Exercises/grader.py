import math
def polysum(n,s):
    area = (0.25 * n * s**2)/math.tan(math.pi/n)
    perimiter = n * s
    return round(area + (perimiter**2),4)
