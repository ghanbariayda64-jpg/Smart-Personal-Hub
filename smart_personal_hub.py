# ============================================================
# PROJECT: SMART PERSONAL HUB 
# DESCRIPTION: Integrated Financial and Fitness Tracker
# FEATURES: Data Persistence, Error Handling, and Menu Navigation 
# ============================================================ 
def get_user_menu_choice():
    """Displays the main menu and returns the user's choice.""" 
    while True: 
        print("\n" + "="*30)
        print(" SMART PERSONAL HUB ")
        print("="*30) 
        print("1. Financial Tracker (Income & Expenses)")
        print("2. Fitness & Calorie Tracker")
        print("3. View Financial History") 
        print("4. View Fitness History") 
        print("5. Exit") 
        print("="*30)
        user_input = input("Enter a number (or type 'stop' to finish): ")
        if user_input.strip().lower() == 'stop':
            return 'stop' 
        try: 
            choice = int(user_input) 
            return choice 
        except ValueError: 
            print("❌ Invalid input! Please enter a number.") 
def get_income():
    """Handles user input for income with error handling."""
    while True: 
        user_input = input("Enter your income (or type 'stop'): ")
        if user_input.strip().lower() == 'stop':
            return 'stop'
        try: 
            return int(user_input)
        
        except ValueError: 
            print("❌ Please enter a valid number.") 
def get_expenses(): 
    """Handles user input for expenses with error handling.""" 
    while True:
        user_input = input("Enter your expenses (or type 'stop'): ") 
        if user_input.strip().lower() == 'stop':
            return 'stop' 
        try: 
            return int(user_input) 
        except ValueError: 
            print("❌ Please enter a valid number.") 
def run_financial_tracker(): 
    """Calculates balance and saves financial records to a file."""
    print("\n--- 💰 Financial Tracker ---")
    income =get_income()
    if income == 'stop': return 
    expenses = get_expenses() 
    if expenses == 'stop': return 
    remaining = income - expenses
    print(f"\n✅ Your remaining balance is: {remaining}")  
    try: 
        file = open("financial_history.txt", "a") 
        file.write(f"Income: {income}, Expense: {expenses}, Remaining: {remaining}\n") 
        file.close() 
        print("💾 History saved to file!") 
    except Exception as e:
        print(f"❌ Error saving to file: {e}") 
    if remaining > 50: 
        print("Great job! You saved some money! 🎉")
    else:
        print("Be careful with your spending! ⚠️")
def run_calorie_tracker(): 
    """Calculates calorie intake and saves fitness records to a file."""
    print("\n--- 🥗 Fitness & Calorie Tracker ---") 
    calorie_limit = 2000 
    total_calories = 0 
    print(f"Your daily limit is: {calorie_limit} kcal")
    print("Enter calories eaten (or type 'stop' to finish):") 
    while True:
        user_input = input("Enter calories: ") 
        if user_input.strip().lower() == 'stop':
            break
        try:
            amount = int(user_input) 
            total_calories += amount 
            print(f"Current total: {total_calories} kcal")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
          
    print(f"\n📊 Total calories consumed: {total_calories} kcal") 
    if total_calories <= 1500:
        print("Bravo! You can eat a treat! 🍪")
    elif total_calories <= calorie_limit: 
        print("Great job! You stayed within your limit! 🌟")
    else: 
        print("Stop eating and go exercise! 🏃‍♂️⚠️")
    try: 
        file = open("fitness_history.txt", "a") 
        file.write(f"Total calories: {total_calories} kcal\n") 
        file.close()
        print("💾 Fitness history saved to file!") 
    except Exception as e: 
        print(f"❌ Error saving to file: {e}")
def show_history(): 
    """Reads and displays the financial history from the file."""
    try: 
        file = open("financial_history.txt", "r") 
        content = file.read() 
        print("\n--- 📜 Your Financial History ---") 
    if content.strip() == "": 
        print("The history file is empty.")
    else: 
        print(content) file.close()
    except FileNotFoundError: 
        print("\n⚠️ No history found yet. Start tracking your money first!") 
def show_fitness_history(): 
    """Reads and displays the fitness history from the file.""" 
    try: 
        file = open("fitness_history.txt", "r") 
        print("\n--- 📜 Your Fitness History ---")
        content = file.read() 
    if content.strip() == "": 
        print("The history file is empty.")
    else:
        print(content) file.close() 
    except FileNotFoundError: 
        print("\n⚠️ No history found yet. Start tracking your fitness first!")  
def main():
    """Main execution loop of the application."""
    while True: 
        choice = get_user_menu_choice()
        if choice == 'stop': 
            print("\nExiting the program. Goodbye! 👋")
            break 
        elif choice == 1: 
            run_financial_tracker()
        elif choice == 2:
            run_calorie_tracker() 
        elif choice == 3: 
            show_history() 
        elif choice == 4: 
            show_fitness_history() 
        elif choice == 5: 
            print("\nExiting the program. Goodbye! 👋") 
            break 
        else: 
            print("❌ Invalid choice! Please select a number.") 
if __name__ == "__main__":
    main()         

          
          
          

