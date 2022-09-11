#1. Write a Python Program to Find the Factorial of a Number?

number = int(input("Enter the number: "))

factorial = 1

if number < 0:
    print("there is no factorial for negative numbers")

elif number == 0:
    print("The factorial for 0 is 1")

else :
    for i in range (1,number + 1):
         factorial = factorial*i
    print("Required factorial of  ", number," is ", factorial)





#2. Write a Python Program to Display the multiplication Table?

number = int(input("Enter the number you want to generate a multiplication table for, then hit the `enter` key: "))
Range = range(1,11)
for i in Range:
    result = number * i
    print(number," * ",i," = ",result)




#3. Write a Python Program to Print the Fibonacci sequence?

nth_term = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nth_term <= 0:
   print("Please enter a positive integer")
elif nth_term == 1:
   print("Fibonacci sequence upto",nth_term,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nth_term:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1






#4. Write a Python Program to Check Armstrong Number?

number = int(input("Enter a number: "))

sum = 0

temporary_number = number
while temporary_number > 0:
   digit = temporary_number % 10
   sum += digit ** 3
   temporary_number //= 10

if number == sum:
   print(number,"is an Armstrong number")
else:
   print(number,"is not an Armstrong number")





#5. Write a Python Program to Find Armstrong Number in an Interval?

lower_limit = int(input("enter lower limit for armstrong number:  "))
upper_limit = int(input("enter upper limit for armstrong number:  "))

if lower_limit < upper_limit:
    for i in range(lower_limit, upper_limit + 1):

        order = len(str(i))

        sum = 0

        temp = i
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if i == sum:
            print(i)
else:
    lower_limit = lower_limit + upper_limit

    upper_limit = lower_limit - upper_limit
    lower_limit = lower_limit - upper_limit

    for i in range(lower_limit, upper_limit + 1):

        order = len(str(i))

        sum = 0

        temp = i
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if i == sum:
            print(i)




#6. Write a Python Program to Find the Sum of Natural Numbers?


number = int(input("Enter a number:  "))

if number < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(number > 0):
       sum += number
       number -= 1
   print("The sum is", sum)