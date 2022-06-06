monthlyInterstRate = annualInterestRate/12
minimumFixedMonthlyPayment = 0
newbalance = balance
while balance > 0:
    minimumFixedMonthlyPayment = minimumFixedMonthlyPayment + 10
    balance = newbalance
    for i in range(12):
        monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
print('Lowest Payment:', minimumFixedMonthlyPayment)
