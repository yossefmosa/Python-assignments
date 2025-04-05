""""
pyramid_rows =int(input("enter number of rows :"))
pyramid_symbol=input ("enter symbol :")

for x in range(1,pyramid_rows+1) :
    print(" "*(pyramid_rows-x),pyramid_symbol*(x))


""""""""""""""""""""""""
pyramid_rows =int(input("enter number of rows :"))
pyramid_symbol=input ("enter symbol :")

Mario_pyramid=[" "]*pyramid_rows
for x in range(len(Mario_pyramid)) :
    Mario_pyramid.pop(0)
    Mario_pyramid.append(pyramid_symbol)
    print("".join(Mario_pyramid))

"""""
def Mario_pyramid(x,y) :
    x=int(x)
    for i in range (1,x+1) :
        print(" "*(x-i),y*(i))   

Mario_pyramid ("4","#")