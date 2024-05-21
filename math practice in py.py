import time

def get_positive_integer(prompt):
     while True:
          try:
               value = int(input(prompt))
               if value > 0:
                    return value
               else: 
                    print("Please enter a positive integer")
          except ValueError:
               print("Invalid input. Please input a positive integer")

print("Today I will show you the beauty of the Collatz Conjecture")

collatz = get_positive_integer("Give me any positive integer: ")
counter = 0

while collatz != 1:
    print(collatz)
    if (collatz % 2) == 0:
         collatz = collatz // 2
    else:
         collatz = (collatz * 3) + 1
    counter += 1
    time.sleep(1)
    

print(collatz)

print("As you can see, no matter which positive integer you choose the algorithm will always end at 1")
print("It took the Collatz Conjecture " + str(counter) + " iterations to get to 1")






