#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
import math

f=float(input("Enter the first price: "))
s=float(input("Enter the second price: "))
t=float(input("Enter the third price: "))
a=float(input("Enter the fourth price: "))
w=float(input("Enter the fifth price: "))

t=f+s+t+a+w
tax=t*(12/100)
tt=t+tax

print(f"Your subtotal is ${t} and your taxes total ${format(tax, '.2f')} for a total of ${format(tt, '.2f')}")