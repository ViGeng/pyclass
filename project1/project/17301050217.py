import math

def computer_right_triangle_permeter(radius,height):
    permeter=radius+height+math.sqrt(radius**2+height**2)
    return permeter

def computer_right_triangle_area(radius,height):
    area=radius*height/2
    return area

def computer_cone_surface(radius,height):
    surface=math.pi *radius*(radius+math.sqrt(radius**2+height**2))
    return surface

def computer_cone_volume(radius,height):
    volume=math.pi*radius**2*height/3
    return volume

def main():
    radius=input("请输入直角三角形的底边长度 ==>")
    height=input("请输入直角三角形的高长度 ==>")
    radius=float(radius)
    height=float(height)
    permeter=computer_right_triangle_permeter(radius,height)
    area=computer_right_triangle_area(radius,height)
    surface=computer_cone_surface(radius,height)
    volume=computer_cone_volume(radius,height)

    print()
    print('-'*40)
    print()
    print('直角三角形的底边长 = %.3f' % radius)
    print('直角三角形的高长 = %.3f' % height)
    print('直角三角形的表面积 = %.3f' % area)
    print('直角三角形的周长 = %.3f' % permeter)
    print('锥形的面积 = %.3f ' % surface)
    print('锥型的体积 = %.3f' % volume)
    print()
    print('-'*40)

if __name__=='__main__':
    main()
























