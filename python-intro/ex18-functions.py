def helloworld(name):
    greeting = "Hello, " + name
    print(greeting)


helloworld("Operation Code")

helloworld("1701")

def sum( arg1, arg2 ):
   total = arg1 + arg2
   print("Inside the function: " + str(total))
   return total

first_sum = sum(4, 2)
print("first_sum: " + str(first_sum))

second_sum = sum(20, 11)
print("second_sum: " + str(second_sum))