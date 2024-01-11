#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, mul, div, sub
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    match operator:
        case "+":
            func = add
        case "-":
            func = sub
        case "*":
            func = mul
        case "/":
            func = div
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print("{} {} {} = {}".format(a, operator, b, func(a, b)))

# careful ./100-.. 1 \* 2 not 1 * 2 in bash xD
