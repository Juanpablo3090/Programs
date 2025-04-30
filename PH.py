# PH LEVEL CALCULATOR
# -------------------------------------------------------------------------------------------

print("---------------------------------------")

while True:
   ph = int(input("enter a value between 7 to 14: "))
   if ph > 7:
      print("Basic")

   elif ph < 7:
      print("Acidic")
      
   else:
      print("Neutral")