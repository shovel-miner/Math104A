#4
#a
lst = [-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lst)
#b
def function(lst):
    lst2 = []
    for i in lst:
        if i >  0 and i%3 == 2:
            lst2.append(i)
            print(lst2)
    return lst2
function(lst)
lst3 = function(lst)
#c
def function2(lst3):
    lst4 = lst3[::3]
    print(lst4)
    return lst4
function2(lst3)
#d
copy_lst1 = lst
copy_lst1[-2] = 100
print(copy_lst1) # They remained different from the second to last number with the original unchanged compared to the copy list. 

#5
# All others from a to c would works fine. However, you can't achieve what is done in 4d with a tuple. But, you can a tuple into a list, do what is done in 4e then reconvert it into tuple

#6
#a
dimensions = {"width":10.0,"height":30.0}
#b
def dimensions_cal(width,height):
    area = width * height
    print(area)
    return area
dimensions_cal(dimensions['width'],dimensions['height'])
dimensions_cal(15.0,25.0)



