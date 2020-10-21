#!/usr/bin/python3
# Program to calculate the total amount accured after a period of compounding interest on a Principal

# Written Expression
# A = P(1+r/n)^nt

p = int(input("What is the principal that you will be investing? (Ex: 1000): "))
r = int(input("What is the interest rate expected(in decimal)? (Ex: 10): "))
n = int(input("How many times does the interest compound each year? (Ex: 2): "))
t = int(input("How many years will you investing? (Ex: 5): "))

A = p*((1+(r/100)/n)**(n*t))
# The total amount that you will recieve at the end of 5 years is 1628.894626777442
print("The total amount that you will recieve at the end of {} years is ${}".format(t,A))
