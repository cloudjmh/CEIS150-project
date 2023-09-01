# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Created by Justin Haag on 9/1/2023

count = 0
amountsum = 0
fullname = str(input("What is your full name?: "))
minimumprice = float(input("What is the minimum price?: "))
price_list = [69.0, 71.0, 84.9, 91.0, 67.4, 81.2, 84.8, 58.8,79.3, 101.2]
for price in price_list:
    amountsum += price
    if price > minimumprice:
        count += 1

print("Hello,", fullname + ", the minimum price is", "${:,.2f}".format(minimumprice) + ".")
print("There are", count ,"prices greater than the minimum price.")
print("The total price is ","${:,.2f}".format(amountsum) + ".")
