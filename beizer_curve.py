import numpy as np

def beizer(x1=0, y1=0, x2=1, y2=1, step=0.1, time=1):
    # handling integer and float
    x1 = float(x1); x2 = float(x2); y1 = float(y1); y2 = float(y2); step = float(step)
    # y-y1 = ((y2-y1)/(x2-x1)) * (x-x1)
    # y-y1 = slope * (x-x1)
    slope = (y2-y1)/(x2-x1)
    # initializing list for new co-ordinates of the points
    new_points = []
    print(x2)


    for x in range(x1,x2,step):
        y = (slope*(x-x1))+y1
        new_points.append((x,y))
    
    return new_points

new_points = beizer()

print(new_points)