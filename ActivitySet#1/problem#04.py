# Conditional Execution

hrs = input("Enter hours: ")
rate = input("Enter rate per hour: ")
try:
  Working = float(hrs)
  PPW = float(rate)
except:
  print("Enter in numeric form :(")
  quit()
if Working > 40:
  bonusrate = PPW * 1.5
  bonuspay = (Working - 40) * bonusrate
  pay = ((Working - (Working - 40)) * PPW) + bonuspay
else:
  pay = Working * PPW
print("Your pay is: $", pay)