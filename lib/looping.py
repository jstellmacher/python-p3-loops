#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    # for i in range(10):
    #     print(i-1)
    x=10
    while(x > 0):
        print(x)
        x-=1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    squared_list = [num * num for num in int_list]
    return squared_list
    # pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    # pass
