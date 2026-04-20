def calculator():
    print("Simple Calculator")
    print("Choose operation:")
    print("A - Add (+)")
    print("B - Subtract (-)")
    print("C - Multiply (x)")
    print("D - Divide (/)")
    
    choice = input("Enter choice (A/B/C/D): ").strip().upper()
    
    if choice not in ['A', 'B', 'C', 'D']:
        print("Invalid choice!")
        return
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number!")
        return
    
    if choice == 'A':
        op_sym = '+'
        result = num1 + num2
    elif choice == 'B':
        op_sym = '-'
        result = num1 - num2
    elif choice == 'C':
        op_sym = 'x'
        result = num1 * num2
    elif choice == 'D':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        op_sym = '/'
        result = num1 / num2
    
    print(f"{num1} {op_sym} {num2} = {result}")

if __name__ == "__main__":
    calculator()
