import math

def compute_right_triangle_perimeter(radius,height):
    perimeter=radius+height+math.sqrt(radius**2+height**2)
    return perimeter

def compute_right_triangle_area(radius,height):
    area=float(0.5)*radius*height
    return area

def compute_cone_surface(radius,height):
    surface=math.pi*radius*(radius+math.sqrt(radius**2+height**2))
    return surface

def compute_cone_volume(radius,height):
    volume=math.pi*radius**2*height/3
    return volume

def main():
    radius=float(input('请输入直角三角形的底边长度==>'))
    height=float(input('%-14s'%'请输入直角三角形的高长度'+'==>'))

    perimeter=compute_right_triangle_perimeter(radius,height)
    area=compute_right_triangle_area(radius,height)
    surface=compute_cone_surface(radius,height)
    volume=compute_cone_volume(radius,height)

    print()
    print('-'*40)
    print()
    print('%16s'%'直角三角形的底边长=','%8.3f'%radius)
    print('%17s'%'直角三角形的高长=','%8.3f'%height)
    print('%17s'%'直角三角形的面积=','%8.3f'%area)
    print('%17s'%'直角三角形的周长=','%8.3f'%perimeter)
    print('%19s'%'锥形的表面积=','%8.3f'%surface)
    print('%20s'%'锥形的体积=','%8.3f'%volume)
    print()
    print('-'*40)
    
if __name__=='__main__':
    main()
