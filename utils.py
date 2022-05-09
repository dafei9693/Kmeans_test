import math

def cal_distance(a,b):
    x=0
    for i in range(len(a)):
        x = x+pow(a[i]-b[i],2)
    return pow(x,1/2)




