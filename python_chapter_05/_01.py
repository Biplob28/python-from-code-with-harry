mydict= {
    "kya haal he":"how are you",
    "khana khaya":"did you eat food",
    "nind aarahi he":"I am sleepy",

"muje aaba jana he":"i need to go now",
"chal theek he":"its ok"


}
print(mydict.get("kya haal he"))
print("the options are",mydict.keys())
a=input("write the hindi words that need to be translated\n")
print("the meaning of word is\n",mydict.get(a))
