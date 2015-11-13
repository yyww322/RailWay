balance = 999999
annualInterestRate = 0.18
def bank(minipay,balance,annualInterestRate):
    monthlyPaymentRate = annualInterestRate/12
    for mon in range(1,13) :
        balance=(balance-minipay)
        balance=balance+annualInterestRate*balance/12
    return balance
mon_low=int(balance*100/12)-1
mon_up=int(100*balance*((1+annualInterestRate/12)**12)/12)+1
minipay=int((mon_low+mon_up)/2) #minipay is use cent
mid_ans_1=bank(float(minipay)/100,balance,annualInterestRate);
mid_ans_0=bank(float(minipay-1)/100,balance,annualInterestRate);
while ((mid_ans_1>0)or(mid_ans_0<0)) :
    if(mid_ans_0<0) :
        mon_up=minipay
        minipay=int((mon_low+mon_up)/2)
    else:
        mon_low=minipay
        minipay=int((mon_low+mon_up)/2)
    mid_ans_1=bank(float(minipay)/100,balance,annualInterestRate);
    mid_ans_0=bank(float(minipay-1)/100,balance,annualInterestRate);
    print(" low = "+str(mon_low)+" up = "+str(mon_up))
print("Lowest Payment: "+str(float(minipay)/100))
