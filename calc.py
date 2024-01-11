first =input("Enter the First value")
second =input("Enter the Second")
first=int(first)
second=int(second)
print("-----press keys opreaters(+,-,*,/,//,**)")
opreators=input("Enter yor opreators:")
if opreators=="+":
    print(first+second)
elif opreators =="-":
    print(first-second)
elif opreators =="*":
    print(first*second)
elif opreators =="/":
    print(first/second)
elif opreators =="//":
    print(first//second)
elif opreators =="**":
    print(first**second)
else:
    print("Syntax ERROR")
