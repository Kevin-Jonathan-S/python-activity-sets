# Conditional Execution

hrs = input("Enter hours: ")
rate = input("Enter rate per hour: ")
try:
  float = int(hrs)
  float = int(rate)
except:
  print("Enter in numeric form :(")
  quit()
if hrs > 40:
  bonusrate = rate * 1.5
  bonuspay = (hrs - 40) * bonusrate
  pay = ((hrs - (hrs - 40)) * rate) + bonuspay
else:
  pay = hrs * rate
print("Your pay is: $", pay)