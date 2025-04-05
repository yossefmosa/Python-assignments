
"""""

your_array =[]
for x in range(5) :
    element=input("enter one element :")
    while not element.isdigit() :
        element=input("enter a valid element :") 
    element=int(element)
    your_array.append(element)

descending_order=sorted(your_array)
ascending_order=sorted(your_array, reverse=True)

print(descending_order)
print(ascending_order)

"""

def create_array_of_elements (x) :
    your_array =[]
    for i in range(x) :
        element=input("enter one element :")
        while not element.isdigit() :
            element=input("enter a valid element :") 
        element=int(element)
        your_array.append(element)

    print(f"descending_order is {sorted(your_array)}" )
    print(f"ascending_order is {sorted(your_array, reverse=True)}" )

create_array_of_elements (5)