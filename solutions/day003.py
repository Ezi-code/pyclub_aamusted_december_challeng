# Ezi-code
def calculate_area(base, height):
    area = 0.5 * base * height
    return area


def main():
    try:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        calculate_area(base, height)
    except ValueError:
        print("Invalid input! ")


if __name__ == "__main__":
    main()
