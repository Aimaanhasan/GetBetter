#WEEK01

#Ques01

def Asterik(lst):
    
    maximum = len(lst[0])
    
    for i in lst:
        if len(i)>maximum:
            maximum = len(i)
    print('* '*maximum)
    
    for i in lst:
        spaces = 2*maximum-4-len(i)
        print( '* ' + i.capitalize() + spaces * ' ' + '*' )
    print('* '*maximum)
    return None


#Asterik(['have','a','good','day'])

#Ques02


def song():
    a= "bottle"
    b="no more"
    for i in range(99,2,-1):
        print(str(i)+" bottles of beer on the wall, " + str(i) + " bottles of bear");
        print("Take one down and pass it around, " + str(i-1) + " bottles of beer on the wall")
    print("2 bottles of beer on the wall, 2 bottles of beer");
    print("Take one down and pass it around, 1 bottle of beer on the wall")
    print("1 bottle of beer on the wall, 1 bottle of beer");
    print("Take one down and pass it around, no more bottles of beer on the wall")
    print("No more bottle of beer on the wall, no more bottles of beer");
    print("Go to the store and buy some more, 99 bottles of beer on the wall.");
#song()
