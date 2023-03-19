sub1=int(input("enter the mrks of subject 1:"))
sub2=int(input("enter the mrks of subject 2:"))
sub3=int(input("enter the mrks of subject 3:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have less than 33 in your each subject")
else:
    print("you have passed each subject")
if(sub1+sub2+sub3)/3>=40:
    print("you are pass congrulation")
else:
    print("you are fail sorry please read and practice more in home ")