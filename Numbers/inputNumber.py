salary = input("Salary: ")
bonus = input("Bonus: ")

paycheckAmt = float(salary) + float(bonus)

print(paycheckAmt)

L = input("Loan: ")
i = input("Interest: ")
i = float(i)/100
n = input("Number of Payement: ")
monthPay = float(L) *(i*(1+i)) / ((1+i)*int(n)-1)


