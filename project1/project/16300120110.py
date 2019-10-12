import math  
    
def compute_right_triangle_area( radius , height ):
    return 1/2 * radius * height

def compute_right_triangle_perimeter ( radius , height ):
    return radius + height + math.sqrt(radius * radius + height * height)

def compute_cone_surface( radius , height ):
    return math.pi * radius * ( radius + math.sqrt ( radius * radius + height * height ) )

def compute_cone_volumn ( radius, height ): 
    return math.pi * radius * radius * height / 3

def standard_output(radius , height):
    print ("-----------------------------------------------")
    print ("直角三角形的底边长" , " = %14.3f" % radius)
    print ("  直角三角形的高长" , " = %14.3f" % height)
    
    area = compute_right_triangle_area( radius , height )
    print ("  直角三角形的面积",  " = %14.3f" % area)

    perimeter = compute_right_triangle_perimeter (radius , height )
    print ("  直角三角形的周长",  " = %14.3f" % perimeter)

    surface = compute_cone_surface( radius , height )
    print ("      锥形的表面积" , " = %14.3f" % surface)

    volumn = compute_cone_volumn (radius, height )
    print ("        锥形的体积",  " = %14.3f" % volumn)

    print("-----------------------------------------------")


def main():
    
    radius = float ( input ("请输入直角三角形的底边长度 ==>" ))
    height = float ( input ("请输入直角三角形的高长度   ==>" ))
    
    standard_output(radius , height)


if __name__ == "__main__":
    main( )

