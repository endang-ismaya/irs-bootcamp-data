# Functions in Dictionary


def add(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def division(num1: int, num2: int) -> float:
    return num1 / num2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    ":": division,
}


while True:
    num1 = int(input("Masukkan number 1: "))
    num2 = int(input("Masukkan number 2: "))
    op = input("Pilih operator: (+, -, *, :) ")

    fn_op = operators.get(op, None)

    if fn_op is None:
        print("Kamu tidak memasukkan operator yang valid!")

    else:
        result = fn_op(num1, num2)
        print(f"{num1} {op} {num2} = {result}")

    print("\n")
