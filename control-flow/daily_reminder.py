# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message components
priority_message = ""
time_sensitive_message = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        priority_message = f"'{task}' is a **high priority** task"
    case "medium":
        priority_message = f"'{task}' is a **medium priority** task"
    case "low":
        priority_message = f"'{task}' is a **low priority** task."
    case _:
        priority_message = f"'{task}' has an **unspecified priority**" # Handles unexpected input

# Modify reminder if the task is time-bound
if time_bound == "yes":
    time_sensitive_message = " that requires immediate attention today!"
elif time_bound == "no":
    if priority == "low":
        time_sensitive_message = " Consider completing it when you have free time."
    else:
        time_sensitive_message = " that can be done at your convenience."
else:
    time_sensitive_message = " (time-bound status unclear)."


# Provide a Customized Reminder
print(f"Reminder: {priority_message}{time_sensitive_message}")