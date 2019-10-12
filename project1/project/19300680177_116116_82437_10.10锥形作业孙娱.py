import math

def compute_right_triangle_perimeter(height,radius):
    perimeter=radius+height+((radius)**2+(height)**2)**(1/2)
    return perimeter

def compute_right_triangle_area(height,radius):
    area=(1/2)*radius*height
    return area

def compute_cone_surface(height,radius):
    surface=math.pi*radius*((radius+((radius)**2+(height)**2)**(1/2)))
    return surface

def compute_cone_volume(height,radius):
    volume=math.pi*(radius**2)*height/3
    return volume


def main():
    radius=input("请输入直角三角形的底边长度==>")
    height=input("请输入直角三角形的高长度  ==>")
    radius=float(radius)
    height=float(height)
    perimeter=compute_right_triangle_perimeter(height,radius)
    area=compute_right_triangle_area(height,radius)
    surface=compute_cone_surface(height,radius)
    volume=compute_cone_volume(height,radius)

    print()
    print('-'*40)
    print()
    print("直角三角形的底边长=%.3f"%radius)
    print("  直角三角形的高长=%.3f"%height)
    print("  直角三角形的面积=%.3f"%area)
    print("  直角三角形的周长=%.3f"%perimeter)
    print("      锥形的表面积=%.3f"%surface)
    print("        锥形的体积=%.3f"%volume)
    print()
    print('-'*40)

if __name__=='__main__':
    main()








    
