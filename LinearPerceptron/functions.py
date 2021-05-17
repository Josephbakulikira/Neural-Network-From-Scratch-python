width,height = 1000, 1000

def Activate(value):
    if value >= 0:
        return 1
    else:
        return -1

def translate(value, min1, max1, min2, max2):
    return min2 + (max2-min2) * ((value - min1)/ (max1 - min1))

def lineFunction(x):
    # wkt y = mx + b
    return 0.45 * x + 0.3
