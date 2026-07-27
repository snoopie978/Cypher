tool_name = "calculator"


def calc():

    def add(num1, num2):
        return num1 + num2

    def sub(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2


    math_dict = {
        "add": add,
        "subtract": sub,
        "multiply": multiply,
        "divide": divide
    }


    command = input("Cypher Calculator > ")

    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))


    if command in math_dict:
        print(math_dict[command](num1, num2))

    else:
        print("Unknown calculation")


def run():
    calc()