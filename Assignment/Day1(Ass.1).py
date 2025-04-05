
""""
vowles="aeiou"
tested_text=input("enter the text :")
counter=0
for x in tested_text :
    if x in vowles :
        counter+=1
print(counter)

""""""""""""

def check(x) :
    x= input(" enter text :")
    vowels="aeiou"
    counter =0
    for i in x :
        if i in vowels :
            counter+=1
    return counter 

print(check("x"))"

"""

def number_of_vowles(x) :
    vowles="aeiou"
    counter=0
    for i in x :
        if i in vowles :
            counter+=1
    return counter


print(number_of_vowles("meaning"))


