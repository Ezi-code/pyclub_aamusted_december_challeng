def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    number = int(input("Enter a number: "))
    factorial(number)


if __name__ == '__main__':
    main()  