monthlyInterstRate = annualInterestRate/12
for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterstRate * monthlyUnpaidBalance)
print(round(balance,2))
