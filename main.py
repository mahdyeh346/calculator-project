import calculator

def show_menu():
    print("\n" + "="*40)
    print("         CALCULATOR")
    print("="*40)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")
    print("="*40)

def get_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    print("Starting calculator program...")
    while True:
        show_menu()
        choice = input("Choose operation (1-7): ")
        
        if choice == '7':
            print("Finished!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            a, b = get_numbers()
            if a is None or b is None:
                continue
            
            if choice == '1':
                result = calculator.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == '2':
                result = calculator.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == '3':
                result = calculator.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == '4':
                result = calculator.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
            elif choice == '5':
                result = calculator.power(a, b)
                print(f"\nResult: {a} ^ {b} = {result}")
            elif choice == '6':
                result = calculator.modulus(a, b)
                print(f"\nResult: {a} % {b} = {result}")
        else:
            print("Error: Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()