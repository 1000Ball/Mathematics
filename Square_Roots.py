'''Two methods for taking the square root of a number'''


## Slower of the two methods. Coded for fun and proof to self it works
def sqrt_ld(n, decimal):
    '''Taking the square root of a number n via long division method. Decimal
    specifies what decimal place to go to. Python output is limited to 20 digits.'''
    ## Extremey slow for big numbers. Should find a way to do this better
    ## Need to modify the lower bound of initial whole number guess

    answer = None
    divisor = None
    new_divisor = None
    extra_divisor = 0
    add_zeros = 0
    next_digit = None
    power = 0

    ## Only real special case
    if n==0:
        return 0.0
    
    ## Checking if it is a whole number
    if n%1 != 0:
        while n%1 != 0:
            n = 10*n
            extra_divisor += 1
        n = int(n)

    ## Attempting to reduce guesses in next session by calling every multitude of 10
    ## bounded below by 3^<multitude> (approximation for sqrt(10)
    for i in range(1, n):
        if 10**i <= n:
            power += 1
        else:
            break
    
    low = 3**power

    ## Finding closest integer that when squared is nearly n
    for i in range(low,n+1):
        if (i**2) <= n:
            answer = i
            divisor = n // i
            remainder = n - i**2
        else:
            break # necessary to avoid checking every integer


    ## Going through the actual methods
    while add_zeros != decimal:
        inequality = remainder * 100
        divisor = answer * 2
        for i in range(10):
            if ((divisor * 10 + i) * i) <= (inequality):
                new_divisor = (divisor * 10 + i)
                next_digit = i
            else:
                break # reduces runtime

        answer = answer * 10 + next_digit
        remainder = inequality - (new_divisor * next_digit)
        add_zeros += 1

    ## Recursion to handle non-integers
    if extra_divisor != 0:
        extra_divisor = 10**extra_divisor
        extra_divisor = sqrt_ld(extra_divisor, decimal)
        answer = (answer / 10**add_zeros / extra_divisor)
    else:
        answer = (answer / 10**add_zeros)

    return round(answer, decimal)

#---------------------------------------------------------------------------

## Faster method
def sqrt_NR(n, decimal):
    '''Newton-Raphson method (Babylonian method) of calculating square
    roots using a slight bit of calculus'''

    ## Equation derivation:
    ## Solve: f(x) = x**2 - n = 0
    ## f'(x) = 2x
    ## When f(x) intercepts x axis, distance from tangent line x intercept
    ## of f(x) to x value be zero (or close to it).
    ## Step size is equal to f(x)/f'(x)
    ## Thus, need to solve 0 = x - f(x)/f'(x)
    ## 0 = x - ((x**2 - n) / (2x)) = x - ((x/2) - (n/2x))

    extra_divisor = 0

    if n == 0:
       return 0.0

    ## Function gets funky when dealing with numbers less than one
    if n < 1:
        while n%1 != 0:
            n = 10*n
            extra_divisor += 1
        n = int(n)

    function = lambda x: x - ((x/2) - (n/2/x))
    x = n # a square root will never exceed this
    next_x = function(x)

    while (x - next_x) >= 10**(-decimal):
        x = next_x
        next_x = function(x)
        #print(x, next_x) # if you want to see steps taken


    ## Same way other function was handled. Iteration for numbers less than one
    if extra_divisor != 0:
        extra_divisor = 10**extra_divisor
        extra_divisor = sqrt_NR(extra_divisor, decimal)
        answer = (next_x / extra_divisor)
    else:
        answer = (next_x)

    return round(answer, decimal)




    
