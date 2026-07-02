sub1 = int(input("Enter marks of sub1:"))
sub2 = int(input("Enter marks of sub2:"))
sub3 = int(input("Enter marks of sub3:"))
sub4 = int(input("Enter marks of sub4:"))
sub5 = int(input("Enter marks of sub5:"))

total = sub1 + sub2 + sub3 + sub4 + sub5 
percentage = total/5
print("percentage =",percentage)

if sub1 < 35 or sub2 < 35 or sub3 < 35 or sub4 < 35 or sub5 < 35:
    print("failed in subject")
else:
    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Class")
    elif percentage >= 50:
        print("Second Class")
    elif percentage >= 35:
        print("Pass")
    else:
        print("Fail")

