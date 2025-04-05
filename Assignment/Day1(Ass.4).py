
"""""
tab_test= input(" enter number :")
tab_test=int(tab_test)

for i in range (1,tab_test+1) :
    for j in range (1,i+1) :
        print(f"{i} x {j} = {i*j}" )
    print ("_____________")

"""""

def num_of_tables(x) :
    while not x.isdigit():
       x= input(" enter a valid number :")
    x=int(x)
    for i in range (1,x+1) :
        for j in range (1,i+1) :
            print(f"{i} x {j} = {i*j}" )
        print ("_____________")
num_of_tables("10")