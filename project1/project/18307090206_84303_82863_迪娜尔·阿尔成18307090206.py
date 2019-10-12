import math
def compute_right_triangle_perimeter(radius,height):
    perimeter = radius + height + math.sqrt(radius*radius + height*height)
    return perimeter

def compute_right_triangle_area(radius,height):
    area = 0.5*radius*height
    return area

def compute_cone_surface(radius,height):
    surface = math.pi*radius*(radius+math.sqrt(radius*radius + height*height)
    return perimeter

def compute_cone_volume(radius,height)：
    volume = （math.pi*radius*radius*height)/3
    return volume

def main():
    radius = input("请输入三角形的底长==>")
    radius = float(radius)
    height = input("请输入三角形的高==>")
    height = float(height)
    perimeter = compute_right_triangle_perimeter(radius,height)
    area = compute_right_triangle_area(radius,height)
    surface = compute_cone_surface(radius,height)
    volume = compute_cone_volume(radius,height)
    print("三角形的周长 = %.3f" % perimeter)
    print("三角形的面积 = %.3f" % area)
    print("圆锥的表面积 = %.3f" % surface)
    print("圆锥的体积 = %.3f" %volume)

if__name__=='__main__':
    
