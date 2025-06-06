# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Return current_date for potential use in calculate_future_date if needed

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date,
    and prints it in 'YYYY-MM-DD' format.
    """
    while True:
        try:
            num_days_str = input("Enter the number of days to add to the current date: ")
            num_days = int(num_days_str)
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    current_date = datetime.now() # Get current date again to ensure it's fresh for this calculation
    future_date = current_date + timedelta(days=num_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()