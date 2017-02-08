def fibonacci(n):
    """This is documentation string for function. It'll be available by fibonacci.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []

    # 1. Create a variable named 'a' and set it to 1
    a = 1

    # 2. Create a variable named 'b' and set it to 1
    b = 1
    while a < n:
        result.append(a)

        # 3. set a variable 'tmp_var' equal to 'b'

        tmp_var = b
        # 4. set a variable 'b' equal to the sum of 'b' and 'a'
        b = b+a
        # 5. set the variable 'a' to 'tmp_var'
        a = tmp_var

    return result

print(fibonacci(100))
