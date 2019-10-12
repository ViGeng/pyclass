import math

def perimeter(radius, height):
    perimeter = radius + height + math.sqrt(radius**2 + height**2)
    return perimeter

def Area(radius, height):
    Area = 0.5 * radius * height
    return Area

def surface(radius, height):
    surface = math.pi * radius * (radius + math.sqrt(radius**2 + height**2))
    return surface

def volume(radius, height):
    volume = math.pi * radius**2 * height/3
    return volume

def main():
    radius = input('请输入直角三角形的底边长度 ==>')
    radius = float(radius)
    height = input('请输入直角三角形的高长度   ==>')
    height = float(height)
    Area_1 = Area(radius, height)
    perimeter_1 = perimeter(radius, height)
    surface_1 = surface(radius, height)
    volume_1 = volume(radius, height)

    print()
    print('-'*50)
    print()
    print('%15s %2s %10.3f' % ('直角三角形的底边长', '=', radius))
    print('%16s %2s %10.3f' % ('直角三角形的高长', '=', height))
    print('%16s %2s %10.3f' % ('直角三角形的面积', '=', Area_1))
    print('%16s %2s %10.3f' % ('直角三角形的周长', '=', perimeter_1))
    print('%18s %2s %10.3f' % ('锥形的表面积', '=', surface_1))
    print('%19s %2s %10.3f' % ('锥形的体积', '=', volume_1))
    print()
    print('-'*50)

if __name__ == '__main__':
    main()
