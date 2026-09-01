cont = 1

while cont <= 1000:
   if cont % 3 == 0 and cont % 5 == 0:
      print("Fizzbuzz")
   elif cont % 3 == 0:
      print("Fizz")
   elif cont % 5 == 0:
      print("Buzz")
   else:
      print(cont)
   cont += 1