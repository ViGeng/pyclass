

def decorate_text(text):
    box = text.split('\n')
    boxx = [i.rstrip() for i in box]
    print('+','-'*(len(max(boxx))+1),'+',sep='')
    for sts in boxx:
        sts=sts.ljust(len(max(boxx))+1)
        print("{0}{1}{0}".format('|',sts,'|'))
    print('+','-'*(len(max(boxx))+1),'+',sep='')
    pass
    



if __name__ == '__main__':
    print('-'*40)
    print('将输入的文本加上装饰条') 

    text = r'''  The King and Queen of Hearts were seated on their throne when they arrived,      
with a great crowd assembled about them--all sorts of little birds and beasts,   
as well as the whole pack of cards: the Knave was standing before them, in  
chains, with a soldier on each side to guard him; and near the King was the    
White Rabbit, with a trumpet in one hand, and a scroll of parchment in the     
other. In the very middle of the court was a table, with a large dish of tarts            
upon it: they looked so good, that it made Alice quite hungry to look at them--   
`I wish they'd get the trial done,' she thought, `and hand round the     
refreshments!'

  But there seemed to be no chance of this, so she began looking at everything           
about her, to pass away the time.         
    '''
   
    decorate_text(text)
    
