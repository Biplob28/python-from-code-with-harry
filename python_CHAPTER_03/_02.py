letter='''Dear <|Name|>,
you are selected,

Date:<|Date|>
'''

name=input("enter your name\n")
date=input("enter the date\n")
letter = letter.replace("<|Date|>",date)
letter = letter.replace("<|Name|>",name)
print(letter)