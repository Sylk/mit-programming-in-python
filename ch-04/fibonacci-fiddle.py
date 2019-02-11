def fibonacci(n):
    # Xn = Xn-1 + Xn-2
    """Assumes n int >= 0
        Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        # The reason the implementation below didn't work is because computes can't take shortcuts.
        # What that means is that we need to manually do each iteration and store them.

        # x = n - 1
        # y = n - 2
        # z = n * x + n * y
        # return z


def test_fibonacci(n):
    for i in range(n+1):
        print('Fibonacci of ', i, '=', fibonacci(i))


test_fibonacci(14)