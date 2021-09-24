def click(low, high):
    try:
        low_limit = int(low)
        high_limit = int(high)
        if low_limit < 2:
            message = 'Please enter positive numbers bigger than 2!'
        elif low_limit < high_limit:
            primelist = prime_numbers(low_limit, high_limit)
            if len(primelist) != 0:
                message = 'Prime numbers between ' + low + ' and ' + high + ' :\n' + str(primelist)
            else:
                message = 'No prime numbers between ' + str(low) + ' and ' + str(high)
        elif low_limit == high_limit:
            primelist = prime_numbers(low_limit, high_limit)
            if len(primelist) == 1:
                message = low + ' is a prime number!'
            else:
                message = low + ' is not a prime number!'
        else:
            message = 'Please enter the values in asceding order!'
    except:
        message = 'Please enter integer numbers!'
    return message

def prime_numbers(low, high):   
    primes = []
    for num in range(low, high+1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes

if __name__ == '__main__':
    value1, value2 = input('Please enter two integers: ').split()
    print(click(value1,value2))

