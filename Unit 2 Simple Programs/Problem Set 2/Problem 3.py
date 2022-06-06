monthlyInterstRate = annualInterestRate/12
monthlyPaymentLowerBound = balance/12
monthlyPaymentUpperBound = (balance * (1 + monthlyInterstRate)**12) / 12
newbalance = balance
while round(balance) != 0:
    midpoint = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
    balance = newbalance
    for i in range(12):
        monthlyUnpaidBalance = balance - midpoint
        balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
    if balance < 0:
        monthlyPaymentUpperBound = midpoint
    else:
        monthlyPaymentLowerBound = midpoint
print('Lowest Payment:', round(midpoint,2))
