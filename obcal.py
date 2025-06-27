# Valid POI Calculator
def POI2(value):
  if ':' in value:
    tm = value.split(":")
    sum1 = int(tm[0]) + int(tm[1])
    if (sum1 > 9):
      result = int(sum1[0]) + int(sum1[1])
      if [3,6,9] in result:
        print("Your POI is valid")
      else:
        print("Your POI is invalid") 
    elif [3,6,9] in sum1:
      print("Your POI is valid")
    else:
      print("Your POI is invalid") 
  elif ':' not in value:
    val2 = value
    val3 = int(value)
    if (val3> 9):
      sum2 = int(val2[0]) + int(val2[1])
      if sum2 in [3,6,9]:
        print("Your POI is valid")
      else:
        print("Your POI is invalid")
    elif val3 in [3,6,9]:
      print("Your POI is valid")
    else:
      print("Your POI is invalid") 
def POI():
  print(" POI timing in date use 1\n POI timing in time use 2")
  ptm = int(input(" Select :"))
  if (ptm==1):
    time = input("Enter date : ")
    POI2(time)
  elif (ptm==2):
    time = input("Enter time(12:00) : ")
    POI2(time)
  else:
    exit()
POI()