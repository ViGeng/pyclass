import math


def compute_right_triangle_perimeter(r,he):
    perimeter = r + h +(r**2 + h**2)**0.5
    return perimeter
def compute_right_triangle_area(r,h):
    area = 0.5*r*h
    return area
def compute_cone_surface(r,h):
    surface = math.pi*r*( r + ( r**2 +h**2 )**0.5 )
    return surface
def compute_cone_volume(r,h):
    volume = math.pi* r**2 *h/3
    return volume


r = float(input('请输入直角三角形的底边长度 ==> '))
h = float(input('请输入直角三角形的高 ==> '))

def print_line(char):
    print(char * 50)
print_line("-")


def main():
    a=compute_right_triangle_perimeter(r,h)
    b=compute_right_triangle_area(r,h)
    c=compute_cone_surface(r,h)
    d=compute_cone_volume(r,h)
    print('直角三角形的底边长=%.3f'%r)
    print('直角三角形的高长=%.3f'%h)
    print('直角三角形的周长=%.3f'%a)
    print('直角三角形的面积=%.3f'%b)
    print('锥形的表面积=%.3f'%c)
    print('锥形的体积=%.3f'%d)
    print("-" * 50)

if __name__=='__main__':
    main()
