marks=int(input("ENTER YOUR MARKS\n"))
if marks>=90:
    grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade ="B"
elif marks>=60:
    grade ="C"
elif marks>=50:
    grade="D"
elif marks>=40:
    grade="E"
else:
    grade="F"


print("your grade is " + grade)