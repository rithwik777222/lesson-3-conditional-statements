num = int(input("enter number to check:"))

if num>50:
    print("number is greater than 50")
    if num%2==0:
        print("and it is even too")
    else:
        print("and it is an odd")

else:
    print("number is less than 50")