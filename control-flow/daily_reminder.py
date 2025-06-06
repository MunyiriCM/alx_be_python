# daily_reminder.py

# Prompt for task details
task = input("Enter your task for today: ")
priority = input("Set the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Loop just to simulate repetition (runs once here)
for _ in range(1):  # Single iteration to demonstrate loop usage
    match priority:
        case "high":
            reminder = f"🔴 HIGH PRIORITY: {task}"
        case "medium":
            reminder = f"🟡 MEDIUM PRIORITY: {task}"
        case "low":
            reminder = f"🟢 LOW PRIORITY: {task}"
        case _:
            reminder = f"⚪ UNRECOGNIZED PRIORITY for task: {task}"

    # Modify reminder based on time sensitivity
    if time_bound == "yes":
        reminder += " — that requires immediate attention today!"

# Print the customized reminder
print(reminder)
