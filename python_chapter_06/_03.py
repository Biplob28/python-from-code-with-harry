text=input("enter the text\n")
spam= False

if("make a lot of money" in text):
    spam= True
elif("buy now " in text):
    spam= True
elif("suscribe now" in text):
    spam=True
elif("click this"in text):
    spam= True
else:
    spam=False
if(spam):
    print("this is spam \n")
else:
    print("this is not spam")