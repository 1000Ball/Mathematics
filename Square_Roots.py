'''Two methods for taking the square root of a number'''


def sqrt_ld(n, decimal):
    '''Taking the square root of a number n via long division method. Decimal
    specifies what decimal place to go to. Python output is limited to 20 digits.'''

    answer = None
    divisor = None
    new_divisor = None
    extra_divisor = 0
    add_zeros = 0
    next_digit = None

    if 0<n<1:
        while n%1 != 0:
            n = 10*n
            extra_divisor += 1
        n = int(n)


    for i in range(1,n+1):
        if (i**2) <= n:
            answer = i
            divisor = n // i
            remainder = n - i**2
        else:
            break

    while add_zeros != decimal:
        inequality = remainder * 100
        divisor = answer * 2
        for i in range(10):
            if ((divisor * 10 + i) * i) <= (inequality):
                new_divisor = (divisor * 10 + i)
                next_digit = i

        answer = answer * 10 + next_digit
        remainder = inequality - (new_divisor * next_digit)
        add_zeros += 1

    
    if extra_divisor != 0:
        extra_divisor = 10**extra_divisor
        extra_divisor = sqrt_ld(extra_divisor, decimal)
        answer = (answer / 10**add_zeros / extra_divisor)
    else:
        answer = (answer / 10**add_zeros)

    return answer
                
    
