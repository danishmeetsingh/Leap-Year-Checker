year = int(input("Which year do you want to check? "))
div_4 = int(year) % 4
div_100 = int(year) % 100
div_400 = int(year) % 400
if int(div_4) == 0 and int(div_100) != 0:
  print("It is a Leap Year.")
elif int(div_400) == 0:
  print("It is a Leap Year.")
else:
  print("It is not a Leap Year")