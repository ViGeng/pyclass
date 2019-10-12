
 
# File     : pj1_1.py
# Author   : Zhukaixiang 17307130222
# Date     : 2019/9/28

import math

def compute_right_triangle_perimeter(r,h):
    return r + h + math.sqrt( r * r + h * h )

def compute_right_triangle_area(r,h):
    return 0.5 * r * h

def compute_cone_surface(r,h):
    return math.pi * r * ( r + math.sqrt( r * r + h * h ))

def compute_cone_volume(r,h):
    return math.pi * r * r * h / 3

def main():
    r = float(input("请输入直角三角形的底边长度 ==> "))
    h = float(input("请输入直角三角形的高长度   ==> "))
    if r > 0 and h > 0: # 判断是否是大于0
        p = compute_right_triangle_perimeter(r,h)
        a = compute_right_triangle_area(r,h)
        s = compute_cone_surface(r,h)
        v = compute_cone_volume(r,h)
    
        print("直角三角形的底边长 = %10.3f" % r)
        print("  直角三角形的高长 = %10.3f" % h)
        print("  直角三角形的面积 = %10.3f" % a)
        print("  直角三角形的周长 = %10.3f" % p)
        print("      锥形的表面积 = %10.3f" %s)
        print("        锥形的体积 = %10.3f" %v)
    else:
        print("输入直角三角形的底边和高必须大于0")

if __name__ == '__main__':
    main()
