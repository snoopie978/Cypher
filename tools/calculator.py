def calc(): 
    def add(num1, num2):
        result = num1 + num2
        return result
    def sub(num1, num2):
        diff = num1 - num2
        return diff
    def multiply(num1, num2): 
        prod = num1 * num2
        return prod
    def divide(num1, num2):
        quote = num1 / num2
        return quote


    math_dict = {
        "add": add,
        "subtract": sub,
        "multiply": multiply,
        "divide": divide
    }
    print("")
    calc_command = input("Cypher Calculator > ")
    print("")

    def execute_math(calc_command):
        num1 = input("First number: ")
        num2 = input("Second number: ")
        if calc_command in math_dict:
            result = math_dict[calc_command](int(num1), int(num2))
            print(result)
        else:
            print("Unknown Command, enter 'help' to view commands")
    execute_math(calc_command)