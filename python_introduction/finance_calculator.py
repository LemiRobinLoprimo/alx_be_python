#!/bin/bash

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Your monthly savings are $",monthly_savings,".", sep="")
print("Projected savings after one year, with interest, is: $",projected_savings,".", sep="")
