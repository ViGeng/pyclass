def main():
    pocket = int(input ('请输入轮盘赌的pocket编号(0-36)==>'))
    
    
    if not(pocket in range(37)):
        print ('编号不在 [0,36]')
        

    elif pocket >=29 and pocket % 2 == 0:
        print ('编号',pocket,'的pocket颜色为红色')

    elif pocket >=29 and pocket % 2 != 0:
        print ('编号',pocket,'的pocket颜色为黑色')
        
           
                 
    elif pocket >= 19 and pocket % 2 == 0:
        print ('编号',pocket,'的pocket颜色为黑色')
        
    elif pocket >= 19 and pocket % 2 != 0:
        print ('编号',pocket,'的pocket颜色为红色')
        

            
    elif pocket >= 11 and pocket % 2 == 0:
        print ('编号',pocket,'的pocket颜色为红色')
        
    elif pocket >=11 and pocket % 2 != 0:
        print ('编号',pocket,'的pocket颜色为黑色')


            
    elif pocket >= 1 and pocket % 2 == 0:
        print ('编号',pocket,'的pocket颜色为黑色')
        
    elif pocket >= 1 and pocket % 2 != 0:
        print ('编号',pocket,'的pocket颜色为红色')   


          
    else:
        print ('编号',pocket,'的pocket颜色为绿色')

        
 
if __name__ == '__main__':
    main()
