#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i > 0:
        print (i)
        i -=1
    else:
        print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    return [x **2 for x in int_list]

def fizzbuzz():
    # code goes here!
    for num in range(1,101):
        if num % 15 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print  ("Fizz")
        elif num % 5 == 0: 
            print ("Buzz")
        else:
            print(num)
  
