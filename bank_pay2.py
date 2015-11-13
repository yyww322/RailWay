balance = 3329
annualInterestRate = 0.2
def bank(minipay,balance,annualInterestRate):
    monthlyPaymentRate = annualInterestRate/12
    for mon in range(1,13) :
        balance=(balance-minipay)
        balance=balance+annualInterestRate*balance/12
    return balance
minipay=int(balance*annualInterestRate/120)*10
while bank(minipay,balance,annualInterestRate)>0 :
    minipay+=10
print("Lowest Payment: "+str(minipay))
