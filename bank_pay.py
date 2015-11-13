balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minipay=0
totalpaid=0
for mon in range(1,13) :
    minipay=balance*monthlyPaymentRate
    min_int=int(minipay*100+0.5)
    min_ans=float(min_int)/100
    totalpaid+=minipay
    balance=(balance-minipay)
    balance=balance+annualInterestRate*balance/12
    bal_int=int(balance*100+0.5)
    bal_ans=float(bal_int)/100
    print("Month: "+str(mon))
    print("Minimum monthly payment: "+str(min_ans))
    print("Remaining balance: "+str(bal_ans))
total_int=int(totalpaid*100+0.5)
total_ans=float(total_int)/100
print("Total paid: : "+str(total_ans))
print("Remaining balance: "+str(bal_ans))

