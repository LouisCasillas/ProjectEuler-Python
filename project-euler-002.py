# Project Euler #2 - https://projecteuler.net/problem=002
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def give_fibonnaci(num1 = 1, num2 = 2, max_num=100):
    while num1 < max_num:
        yield num1
        num1, num2 = num2, num1 + num2
        
fib_sequence = give_fibonnaci(1,2,4000000)

even_valued_fibs = [ i for i in fib_sequence if (i % 2) == 0]

print(sum(even_valued_fibs))
