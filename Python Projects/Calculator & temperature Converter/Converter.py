def main():
    print("*" * 26)
    print("What services do you need?")
    print("*" * 26)
    print("1. Calculator", "2. Celsius to Fahrenheit","3. Fahrenheit to Celsius", sep = "\n")
    ch = input("Choose a Service: ")
    if not ch.isdigit():
        print("Not digit")
    else:
        if ch == "1":
            calc()
        elif ch == "2":
            cels()
        elif ch == "3":
            fahr()
        else:
            print("Invalid Number")

def calc():
    is_running = True
    while is_running:
        num1 = float(input("Enter a number: "))
        oper = input("Choose one operator (+ - * / %): ")
        num2 = float(input("Enter a second number: "))

        if oper == "+" or oper == "-" or oper == "*" or oper == "/" or oper == "%":
            if oper == "+":
                tot = num1 + num2
                print(f"{tot:.2f}")
            elif oper == "-":
                tot = num1 - num2
                print(f"{tot:.2f}")
            elif oper == "*":
                tot = num1 * num2
                print(f"{tot:.2f}")
            elif oper == "/":
                tot = num1 / num2
                print(f"{tot:.2f}")
            elif oper == "%":
                tot = num1 % num2
                print(f"{tot:.2f}")
            else:
                print("invalid input")
            ask = input("Press Q to quit or Press Enter to Continue: ").lower()
            if ask == "q":
                is_running = False
        else:
            print("Invalid Operator")

def cels():
    is_running = True
    while is_running:
        cel = float(input("Enter a Celsius Degree: "))
        if cel == "":
            print("It cannot be empty, Enter something")
        else:
            tot = cel * 9 / 5 + 32
            print(f"Fahrenheit : {tot:.2f}")
        ask = input("Press Q to quit or Press Enter to Continue: ").lower()
        if ask == "q":
            is_running = False

def fahr():
    is_running = True
    while is_running:
        fah = float(input("Enter a Fahrenheit Degree: "))
        if fah == "":
            print("It cannot be empty, Enter something")
        else:
            tot = fah - 32
            tote = tot * 5/9
            print(f"Celsius: {tote:.2f}")
        ask = input("Press Q to quit or Press Enter to Continue: ").lower()
        if ask == "q":
            is_running = False

main()
