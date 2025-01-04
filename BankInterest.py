#This file is for the Bank Interest question.
print("Welcome to SuperBank!")
sb=float(input("Enter starting balance:"))
air=float(input("Enter annual interest rate:"))
amf=float(input("Enter account maintance fee:"))
n=1
while n<10:
    n=n+1
    print("Year ",n)
    sb=sb+sb*air/100-amf
    print("End of the year balance:",format(sb,'.3f'))








