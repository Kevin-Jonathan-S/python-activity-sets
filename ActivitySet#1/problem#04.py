# Conditional Execution

hrs = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
if hrs > 40:
  bonusrate = rate * 1.5
  bonuspay = (hrs - 40) * bonusrate
  pay = ((hrs - (hrs - 40)) * rate) + bonuspay
else:
  pay = hrs * rate
print("Your pay is: $", pay)