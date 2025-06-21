def divide(num, div):
    if div == 0:
        raise ValueError("Divisor cannot be zero.")

    q = 0
    r = num

    while r >= div:
        r -= div
        q += 1

    print("Quotient: {} Remainder: {}".format(q, r))


# Example usage:
divide(10, 3)  # Output: Quotient: 3 Remainder: 1
