import time
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    banner = f"""
    {Fore.CYAN}+---------------------------+
    |      {Fore.YELLOW}CALCULATOR{Fore.CYAN}      
    +---------------------------+
    """
    print(banner)

def calculator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        
        try:
            num1 = float(input(Fore.GREEN + "Enter first number: " + Style.RESET_ALL))
            num2 = float(input(Fore.GREEN + "Enter second number: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter numbers only." + Style.RESET_ALL)
            time.sleep(2)
            continue
        
        print("\nChoose operation:")
        print(Fore.YELLOW + "1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
        choice = input(Fore.CYAN + "Enter your choice (1-4): " + Style.RESET_ALL)
        
        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print(Fore.RED + "Error! Division by zero is not allowed." + Style.RESET_ALL)
                time.sleep(2)
                continue
            result = num1 / num2
            operation = '/'
        else:
            print(Fore.RED + "Invalid choice! Please select a valid operation." + Style.RESET_ALL)
            time.sleep(2)
            continue
        
        print(Fore.MAGENTA + f"\nResult: {num1} {operation} {num2} = {result}" + Style.RESET_ALL)
        time.sleep(3)

        again = input(Fore.BLUE + "Do you want to perform another calculation? (yes/no): " + Style.RESET_ALL).lower()
        if again not in ['yes', 'y']:
            print(Fore.CYAN + "Thank you for using the calculator! Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    calculator()
