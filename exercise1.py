#1. Write a program that asks for a number N as a user input, and calculates the sum of odd numbers, and the average of even numbers starting from 1 up to and including N.
n = int(input('value: '))
def odd(n):
    total = 0
    for a in range(1,n+1,2):
        total = total + a 
    return print('sum of odd numbers:',total)

def even(n):
    total2 = 0
    div = 0
    hmany= n / 2 
    for b in range(0,n+1,2):
        total2 = total2 + b
        div = total2 / hmany
    return print('average of even numbers:',div) 

odd(n), even(n)


