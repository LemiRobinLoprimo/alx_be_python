#!/bin/bash

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
mon_sav = income - expenses
pro_sav = int(mon_sav * 12 + (mon_sav * 12 * 0.05))
print("Your monthly savings are $",mon_sav,".", sep="")
print("Projected savings after one year, with interest, is: $",pro_sav,".", sep="")
