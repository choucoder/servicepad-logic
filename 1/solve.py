def solve(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


if __name__ == '__main__':
    n = 100
    for i in range(1, n + 1):
        print(solve(i))