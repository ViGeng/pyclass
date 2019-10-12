
#计算直角三角形的周长面积以及锥形的表面积体积

import math

def compute_right_triangle_perimeter(radius,height):
    pertimeter = radius+height+(radius**2+height**2)**0.5
    return pertimeter

def compute_right_triangle_area (radius,height):
    area = 0.5*radius*height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi*radius*(radius+(radius**2+height**2)**0.5)
    return surface

def compute_cone_volume(radius,height):
    volume = math.pi*(radius**2)*height*(1/3)
    return volume 


def main():
   radius = input("请输入直角三角形的底边长度 ==> ")
   radius = float(radius)
   height = input("请输入直角三角形的高长度   ==> ")
   height = float(height)
   pertimeter = compute_right_triangle_perimeter (radius,height)
   area = compute_right_triangle_area(radius,height)
   surface = compute_cone_surface(radius,height)
   volume = compute_cone_volume(radius,height)

   print()
   print('-' * 30)
   print("     直角三角形的底边长 =   %.3f" % radius)
   print("       直角三角形的高长 =   %.3f" % height)
   print("       直角三角形的周长 =  %.3f" % pertimeter)
   print("       直角三角形的面积 =  %.3f" % area)
   print("           锥形的表面积 = %.3f" % surface)
   print("             锥形的体积 = %.3f" % volume)
   print()
   print('-' * 30)

if __name__== '__main__':
    main()
