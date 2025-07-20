

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()


time_msg = ""
if time_bound == "yes":
    time_msg = " that requires immediate attention today!"
else:
    time_msg = ". Consider completing it when you have free time."

match priority:
    case "high":
        print(f"Reminder: '{task}' is a HIGH priority task{time_msg}")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task{time_msg}")
    case "low":
        print(f"Note: '{task}' is a low priority task{time_msg}")
    case _:
        print(f"Note: '{task}' has an unrecognized priority lev")
