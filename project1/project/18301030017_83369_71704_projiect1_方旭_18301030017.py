import math

def compute_right_triangle_perimeter(radius,height):
    perimeter = radius+height+math.sqrt(radius**2+height**2)
    return perimeter  #结束函数运行, 把周长值作为输出结果,但是后面仍然要给perimeter一个定义

def compute_right_triangle_area(radius,height):
    area =0.5*radius*height
    return area

def compute_cone_surface(radius,height):
    surface =math.pi*radius*(radius+math.sqrt(radius**2+height**2))
    return surface

def compute_cone_volume(radius,height):
    volume =math.pi* radius**2 *height/3    #pi必须要写成math.pi, 对于sqrt开根号也是一样
    return volume

def main():
    radius = input ("请输入直角三角形的底边边长==>")
    radius = float(radius)
    height = input ("请输入自己三角形的高长度  ==>")
    height = float(height)
    perimeter= compute_right_triangle_perimeter(radius,height)
    area= compute_right_triangle_area(radius,height)
    surface= compute_cone_surface(radius,height)
    volume= compute_cone_volume(radius,height)

    print()
    print('-'*40)
    print()
    print('直角三角形的底边长 = %7.3f'% radius)
    print('  直角三角形的高长 = %7.3f'% height)
    print('  直角三角形的面积 = %7.3f'% area)
    print('  直角三角形的周长 = %7.3f'% perimeter)
    print('      锥形的表面积 = %7.3f'% surface)
    print('        锥形的体积 = %7.3f'% volume)
    print()
    print('-'*40)

if __name__=='__main__':
    main()
