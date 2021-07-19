# print out a list of numbers from 1-100
# if the number is divisible evenly by 3 we will print out fizz instead of the number
# if the number is divisible evenly by 5 we will print out buzz instead of the number
# if the number is divisible evenly by both 3 and 5 print out fizzbuzz

def fizzbuzz():
    for i in range(1, 16):
        if (i % 5 == 0 and i % 3 == 0):
            print("fizzbuzz")
        elif (i % 3 == 0):
            print("fizz")
        elif (i % 5 == 0):
            print("buzz")
        else:
            print(i)

fizzbuzz()