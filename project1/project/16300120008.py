radius = eval(input('请输入直角三角形的底边长度==>'))
height = eval(input('请输入直角三角形的高长度==>'))

def perimeter(radius,height):
    perimeter = radius + height + ( (radius)**2 + (height)**2)**.5
    return perimeter

def area(radius,height):
    area = 0.5*radius*height
    return area

def surface(radius,height):
    import math
    surface = math.pi*radius*(radius +   ( (radius)**2 + (height)**2)**.5)
    return surface

def volume(radius,height):
    import math
    volume = math.pi*(radius**2)*height/3
    return volume

def main(radius,height):
    p = perimeter(radius,height)
    a = area(radius,height)
    s = surface(radius,height)
    v = volume(radius,height)
    print('\n---------------------------------------------------\n')
    print('直角三角形的底边长 = %10.3f'%radius,sep='')
    print('%10s = %10.3f'%('直角三角形的高长',height),sep='')
    print('%10s = %10.3f'%('直角三角形的面积',a),sep='')
    print('%10s = %10.3f'%('直角三角形的周长',p),sep='')
    print('%12s = %10.3f'%('锥形的表面积',s),sep='')
    print('%13s = %10.3f'%('锥形的体积',v),sep='')
    print('\n---------------------------------------------------\n')

if __name__ == "__main__":
    main(radius,height)

