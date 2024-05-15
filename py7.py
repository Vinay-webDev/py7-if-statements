#if statement,else if statement,else statement
# if statement = a block of code which executes only if it's condition is true

#for that i'll just create a variable with input prompt***

age = input("what is your age? ")
#remember input accepts only strings(str) so we need to type cast

age = int(input("what is your age? "))
if age>= 18:                       # ***if statements must close colons:  ***
    print("you are an adult!")
elif age == 100:                       # **** double equal sign is comparative operator **** if you just use single eqaul means you are just assigning the value! so you got to use double equal in order to comapare values
    print("you are century old!")
elif age<0:
    print("you haven't been born yet!")
else:
    print("you are a child!")

age = int(input("what is your age?: "))  # you must type cast in order to do math on 'str'
if age == 100:
    print ("you are century old!")
elif age >=18:
 print("you are an adult!")
elif age<0:
   print("you haven't been born yet!")
else:
   print("you are a kid lol")
