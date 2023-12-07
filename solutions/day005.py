# Ezi-code
def main():
    degree_celsius = float(input("Enter a degree in Celsius: "))
    convert(degree_celsius)
    return

def convert(degree_celsius):
    fahrenheit = (degree_celsius * 9/5) + 32
    return fahrenheit


if __name__ == "__main__":
    main()