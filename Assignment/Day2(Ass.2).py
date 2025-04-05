
"""""

List_of_table= input(" enter number :")
while not List_of_table.isdigit():
    List_of_table= input(" enter a valid number :")
List_of_table=int(List_of_table)
List2=[]

for i in range (1,List_of_table+1) :
    List1=[]
    for j in range (1,i+1) :
        List1.append(f"{i*j}")  #ممكن نشيل ال f 
    List2.append(List1)
print(List2)

"""""

def List_of_tables(x) :
    while not x.isdigit():
       x= input(" enter a valid number :")
    x=int(x)
    List2=[]
    for i in range (1,x+1) :
        List1=[]
        for j in range (1,i+1) :
            List1.append(f"{i*j}")
        List2.append(List1)
    print(List2)

List_of_tables("10")