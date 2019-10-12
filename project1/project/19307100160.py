import math
def compute_right_triangle_perimeter(r,h):
    result=round(r+h+math.sqrt(r**2+h**2),3)
    return result
def compute_right_triangle_area(r,h):
    result=round(1/2*r*h,3)
    return result
def compute_cone_surface(r,h,l):
    result=round(math.pi*r*l,3)
    return result
def compute_cone_volume(r,h):
    result=round(math.pi*r**2*h/3,3)
    return result
def main():
    r=eval(input('请输入直角三角形的底边长度 ==>'))
    h=eval(input('请输入直角三角形的高长度 ==>'))
    l=r+math.sqrt(r**2+h**2)
    print()
    print('-'*20)
    print()
    print('    直角三角形的周长为 = ',compute_right_triangle_perimeter(r,h))
    print('    直角三角形的面积为 = ',compute_right_triangle_area(r,h))
    print('       锥形的表面积为 = ',compute_cone_surface(r,h,l))
    print('         锥形的体积为 = ',compute_cone_volume(r,h))
    print()
    print('-'*20)
    print()
if __name__=='__main__':
    main()
