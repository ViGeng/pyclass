##Project1
##作者：19级经济学院 应眺


import math
pi=3.14159
def compute_right_triangle_perimeter(radius,height):
    Perimeter=radius+height+math.sqrt(radius**2+height**2)
    return Perimeter

def compute_right_triangle_area(radius,height):
    Area=0.5*radius*height
    return Area

def compute_cone_surface(radius,height):
    Surface=pi*radius*(radius+math.sqrt(radius**2+height**2))
    return Surface

def compute_cone_volume(radius,height):
    Volume=pi*radius**2*height/3
    return Volume

def main():
    radius=input('请输入直角三角形的底边长度 ==>')
    height=input('请输入直角三角形的高长度   ==>')
    radius=float(radius)
    height=float(height)
    print('直角三角形的底边长 ='+'%10.3f' %radius)
    print('  直角三角形的高长 ='+'%10.3f' %height)
    print('  直角三角形的面积 ='+'%10.3f' %compute_right_triangle_area(radius,height))
    print('  直角三角形的周长 ='+'%10.3f' %compute_right_triangle_perimeter(radius,height))
    print('      锥形的表面积 ='+'%10.3f' %compute_cone_surface(radius,height))
    print('        锥形的体积 ='+'%10.3f' %compute_cone_volume(radius,height))
    
if __name__ == '__main__':
    main()
