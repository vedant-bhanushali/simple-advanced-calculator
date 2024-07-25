
def calculator():
    num_times = int(input("Enter number of operands: "))
    operator = input("Enter operator (+, -, *, /): ")

    numbers = []
    for i in range(num_times):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)

    result = numbers[0]
    for i in range(1, num_times):
        if operator == '+':
            result += numbers[i]
        elif operator == '-':
            result -= numbers[i]
        elif operator == '*':
            result *= numbers[i]
        elif operator == '/':
            if numbers[i] != 0:
                result /= numbers[i]
            else:
                print("Error ")
                return
        else:
            print("Invalid try again.")
            return

    print(f"Result of {operator.join(map(str, numbers))}: {result}")

calculator()


