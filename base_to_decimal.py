def get_decimal_to_base(binary_number: int, input_base: int) -> int:
    decimal = 0
    i = 0
    while binary_number > 0:
        rem = binary_number % 10
        decimal += rem * input_base ** i
        i += 1
        binary_number //= 10
    return decimal


try:
    binary_num = int(input("Enter the number : "))
    base = int(input("Enter base : "))
    print("The decimal value is : ", get_decimal_to_base(binary_num, base))
except ValueError:
    print("Invalid input. Please enter only integers.")
