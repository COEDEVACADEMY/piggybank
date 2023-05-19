import os
import time
print("This is my bank ")
runtime=True
balance=0
while runtime==True:
 time.sleep(3)
 os.system('cls')
 print("How can I help you? :")
 print("1 - Insert money")
 print("2 - Take out money")
 print("3 - Display Balance")
 print("4 - Exit")
 choice=input(":")
 if choice=="1":
  os.system('cls')
  amount=input("Enter amount:RM")
  balance=balance+float(amount)
 elif choice=="2":
  os.system('cls')
  amount=float(input("Enter amount:RM"))
  if amount >= balance:
   balance=balance-float(amount)
  else:
    print("Not enough balance")
 elif choice=="3":
  os.system('cls')
  print("Current balance :RM" + str(balance))
 elif choice=="4":
  os.system('cls')
  print("Thank you")
  runtime=False
 else:
  os.system('cls')
  print("Wrong input. try again")
