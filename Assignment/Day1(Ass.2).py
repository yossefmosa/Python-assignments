
""""



# الكود هنا غلط لو كتبت mining 
# مثلا هيطلعلي 1و 1 عشان هو هيدخل يجيب أول مكان لقيمة ال x 
#(الي هي ال1)
tested_text=input("enter the text :")

for x in  tested_text :
    if x == "i" :
       y=tested_text.index(x)
       print(y)  

        

text_test= input(" enter text :")
for x in range(len(text_test)):
    y = text_test[x]
    if y == "i" :
        print (x)
"""
def index_of_string (x) :
    for i in range(len(x)) :
        y = x[i]
        if y == "i" :
           print(i)
        
        
index_of_string ("mining")