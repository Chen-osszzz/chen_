import os

# ================== A. DAILY LOGGING MODULE ==================
# These functions allow the user to log daily activities and health data.

def log_meal(data):
    # Logs user's meal and calorie intake
    food = input("What did you eat today? ")
    calories = input("How many calories did you consume? ")
    data["meal"] = food
    data["calories"] = float(calories)

def log_sleep(data):
    # Logs sleep duration in hours
    sleep = input("How many hours did you sleep? ")
    data["sleep"] = float(sleep)

def log_water(data):
    # Logs water intake in liters
    water = input("How much water did you drink (in liters)? ")
    data["water"] = float(water)

def log_exercise(data):
    # Logs exercise type and duration
    activity = input("What exercise did you do? ")
    duration = input("How long (in minutes)? ")
    data["exercise"] = activity
    data["duration"] = int(duration)

# ================== B. SUMMARY & STATS MODULE ==================
# Functions to load weekly logs and calculate statistics like totals and averages.

def load_logs_for_week():
    # Loads daily logs for day1.txt to day7.txt and extracts relevant metrics
    log_data = {
        "Day": [],
        "Calories": [],
        "Sleep": [],
        "Water": [],
        "Exercise duration": []
    }

    for i in range(1, 8):
        filename = f"day{i}.txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                lines = file.readlines()
                log_data["Day"].append(f"Day {i}")
                for line in lines:
                    key, value = line.strip().split(":", 1)
                    # Sort values into correct lists for stats
                    if key.lower() == "calories":
                        log_data["Calories"].append(float(value))
                    elif key.lower() == "sleep":
                        log_data["Sleep"].append(float(value))
                    elif key.lower() == "water":
                        log_data["Water"].append(float(value))
                    elif key.lower() == "duration":
                        log_data["Exercise duration"].append(float(value))
    return log_data

def calculate_weekly_stats(log_data):
    # Calculates and displays total and average statistics for the week
    def average(lst):
        return sum(lst) / len(lst) if lst else 0

    print("\n📊 Weekly Health Statistics:")
    print(f"Total Calories: {sum(log_data['Calories'])} kcal")
    print(f"Average Calories: {average(log_data['Calories']):.1f} kcal")
    print(f"Total Sleep: {sum(log_data['Sleep'])} hrs")
    print(f"Average Sleep: {average(log_data['Sleep']):.1f} hrs")
    print(f"Total Water: {sum(log_data['Water'])} L")
    print(f"Average Water: {average(log_data['Water']):.1f} L")
    print(f"Total Exercise Duration: {sum(log_data['Exercise duration'])} mins")
    print(f"Average Exercise Duration: {average(log_data['Exercise duration']):.1f} mins")

def calculate_daily_totals(data):
    # Displays the daily summary for the current day's data
    print("\n--- Daily Totals ---")
    print(f"Water: {data.get('water', 0)} L")
    print(f"Calories: {data.get('calories', 0)} kcal")
    print(f"Sleep: {data.get('sleep', 0)} hrs")
    print(f"Exercise: {data.get('exercise', 'None')} for {data.get('duration', 0)} mins")

def generate_weekly_summary():
    # Reads and prints raw log files for each day of the week
    print("\n--- Weekly Summary ---")
    for filename in os.listdir():
        if filename.startswith("day") and filename.endswith(".txt"):
            print(f"\n{filename}:")
            with open(filename, "r") as f:
                print(f.read())

# ================== C. ALERTS & GOALS MODULE ==================
# Warns the user if they miss sleep or water goals and gives health tips.

SLEEP_GOAL = 7.0  # Recommended minimum sleep (hours)
WATER_GOAL = 2.0  # Recommended minimum water intake (liters)

def check_sleep_goal(day_data):
    # Checks if sleep goal was met
    sleep = day_data.get("sleep", 0)
    return sleep < SLEEP_GOAL

def check_water_goal(day_data):
    # Checks if water goal was met
    water = day_data.get("water", 0)
    return water < WATER_GOAL

def suggest_tips(missed):
    # Provides health suggestions based on what was missed
    tips = []
    if "sleep" in missed:
        tips.append("💤 Try sleeping 30 minutes earlier.")
    if "water" in missed:
        tips.append("💧 Don’t forget to drink enough water!")
    return tips

def show_warnings(data_dict):
    # Goes through all days and shows warnings and tips for missed goals
    print("\n⚠️ Health Warnings:")
    found = False
    for day, data in data_dict.items():
        missed = []
        if check_sleep_goal(data):
            missed.append("sleep")
        if check_water_goal(data):
            missed.append("water")
        if missed:
            found = True
            print(f"\n📅 {day}")
            if "sleep" in missed:
                print(f"  ❗ Not enough sleep: {data.get('sleep', 0)} hrs (Goal: {SLEEP_GOAL})")
            if "water" in missed:
                print(f"  ❗ Not enough water: {data.get('water', 0)} L (Goal: {WATER_GOAL})")
            for tip in suggest_tips(missed):
                print("  Tip:", tip)
    if not found:
        print("✅ You met all your goals! Great job!")

# ================== D. CLI MENU & FILE MANAGEMENT ==================
# Main menu interface and file loading/saving for each day's log.

def save_log_to_file(data, filename):
    # Saves a dictionary of data to a text file
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")

def load_log_from_file(filename):
    # Loads data from a file and stores it in a dictionary
    data = {}
    if not os.path.exists(filename):
        return data
    with open(filename, "r") as file:
        for line in file:
            if ":" in line:
                key, value = line.strip().split(":", 1)
                try:
                    value = float(value) if "." in value or value.strip().isdigit() else value
                except:
                    pass
                data[key] = value
    return data

def main_menu():
    # User interface for interacting with the health tracker system
    username = input("Enter your username: ").strip()
    if username == "":
        print("Please enter a valid username.")
        return

    print(f"\nWelcome, {username}!")
    day_number = input("Enter the day number: ").strip()
    filename = f"day{day_number}.txt"

    data = load_log_from_file(filename)
    data["username"] = username
    data["day"] = day_number

    while True:
        # Show options for the user
        print("\n===== Health Tracker Menu =====")
        print("1. Log Water")
        print("2. Log Meal/Calories")
        print("3. Log Sleep")
        print("4. Log Exercise")
        print("5. Show Daily Summary")
        print("6. Save and Exit")
        print("7. Weekly Summary (Raw Logs)")
        print("8. Show Warnings")
        print("9. Show Weekly Stats")

        choice = input("Choose an option: ")

        if choice == "1":
            log_water(data)
        elif choice == "2":
            log_meal(data)
        elif choice == "3":
            log_sleep(data)
        elif choice == "4":
            log_exercise(data)
        elif choice == "5":
            calculate_daily_totals(data)
        elif choice == "6":
            save_log_to_file(data, filename)
            print(f"Data saved to {filename}.")
            break
        elif choice == "7":
            generate_weekly_summary()
        elif choice == "8":
            all_data = {}
            for f in os.listdir():
                if f.startswith("day") and f.endswith(".txt"):
                    all_data[f] = load_log_from_file(f)
            show_warnings(all_data)
        elif choice == "9":
            # Loads and calculates weekly statistics (total + average)
            log_data = load_logs_for_week()
            calculate_weekly_stats(log_data)
        else:
            print("Invalid option. Try again.")

# Entry point for the script
if __name__ == "__main__":
    main_menu()
