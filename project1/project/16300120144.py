import math

def compute_right_triangle_perimeter(radius, height):
    Perimeter = radius + height + math.sqrt(radius ** 2 + height ** 2)
    return Perimeter

def compute_right_triangle_area(radius, height):
    Area = radius / 2 * height
    return Area

def compuete_cone_surface(radius, height):
    Surface = math.pi * radius * (radius + math.sqrt(radius ** 2 + height ** 2))
    return Surface

def compute_cone_volume(radius, height):
    Volume = math.pi * radius ** 2 * height / 3
    return Volume
    
def main ():
    radius = float(input('请输入直角三角形的底边长度 ==> '))
    height = float(input('请输入直角三角形的高长度  ==> '))
    Perimeter = compute_right_triangle_perimeter(radius, height)
    Area = compute_right_triangle_area(radius, height)
    Surface = compuete_cone_surface(radius, height)
    Volume = compute_cone_volume(radius, height)
    
    print('-' * 40)
    print ('''\r
           直角三角形的底边长 =    %.3f\r
             直角三角形的高长 =    %.3f\r
             直角三角形的面积 =    %.3f\r
             直角三角形的周长 =    %.3f\r
                锥形的表面积 =    %.3f\r
                  锥形的体积 =    %.3f\r'''
           % (radius, height, Area, Perimeter, Surface, Volume))
    print('-' * 40)

if __name__ == '__main__':
    main ()

