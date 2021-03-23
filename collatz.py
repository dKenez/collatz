def collatz(n):
    """calculate next number in according to collatz rules"""
    if n % 2:
        n = n*3 + 1
    else:
        n = int(n/2)

    return n


def inv_collatz_odd(n):
    val = (n - 1) / 3
    if val > 0 and val.is_integer() and int(val) % 2:
        return int(val)
    return -1


def inv_collatz_even(n):
    return n * 2


if __name__ == '__main__':
    while True:
        num = int(input("Start number: "))
        iteration = 0

        while True:
            if num == 1:
                break

            print(num)
            num = collatz(num)
            iteration += 1

        print(num)
        print("\nIterations = ", iteration)
