#Task 3: Implementing control structures

#If Statement: positive, neagative, or zero
def check_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

#For Loop: first 10 prime numbers
def ten_prime():
    primes = 0
    for num in range(2, 100):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num)
            primes += 1
        
        if primes == 10:
            break

#While Loop: Sum of all numbers 1 - 100
def sum_to_hundred():
    num = 1
    sum = 0
    while num <= 100:
        sum += num
        num += 1
    
    return sum

