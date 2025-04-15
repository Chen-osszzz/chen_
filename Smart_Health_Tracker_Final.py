import os

# ================== A. DAILY LOGGING MODULE ==================
# Functions in this section handle logging daily inputs from the user.

# Logs meal and calorie intake
def log_meal(data):
    food = input("What did you eat today? ")
    calories = input("How many calories did you consume? ")
    data["meal"] = food
    data["calories"] = float(calories)  # Store calories as float

# Logs sleep duration
def log_sleep(data):
    sleep = input("How many hours did you sleep? ")
    data["sleep"] = float(sleep)  # Store sleep hours as float

# Logs water intake in liters
def log_water(data):
    water = input("How much water did you drink (in liters)? ")
    data["water"] = float(water)  # Store water as float

# Logs type of exercise and its duration in minutes
def log_exercise(data):
    activity = input("What exercise did you do? ")
    duration = input("How long (in minutes)? ")
    data["exercise"] = activity
    data["duration"] = int(duration)  # Store duration as integer

# ================== B. SUMMARY & STATS MODULE ==================
# Function for calculating and displaying weekly average stats

def calculate_weekly_stats():
    print("\n--- Weekly Statistics ---")
    
    # Initialize counters
    total_water = 0
    total_calories = 0
    total_sleep = 0
    total_exercise_duration = 0
    count = 0

    # Loop through files named dayX.txt to accumulate data
    for filename in os.listdir():
        if filename.startswith("day") and filename.endswith(".txt"):
            with open(filename, "r") as file:
                for line in file:
                    if ":" in line:
                        key, value = line.strip().split(":", 1)
                        # Sum values by key
                        if key == "water":
                            total_water += float(value)
                        elif key == "calories":
                            total_calories += float(value)
                        elif key == "sleep":
                            total_sleep += float(value)
                        elif key == "duration":
                            total_exercise_duration += int(float(value))
            count += 1  # Count how many files (days) processed

    if count == 0:
        print("No data found for the week.")
        return
    
    # Calculate and print averages
    print(f"Average Water: {round(total_water / count, 2)} L")
    print(f"Average Calories: {round(total_calories / count, 2)} kcal")
    print(f"Average Sleep: {round(total_sleep / count, 2)} hrs")
    print(f"Average Exercise Duration: {round(total_exercise_duration / count, 2)} mins")

# ================== C. ALERTS & GOALS MODULE ==================
# Constants for daily health goals
SLEEP_GOAL = 7.0  # Target hours of sleep
WATER_GOAL = 2.0  # Target liters of water

# Check if user met the sleep goal
def check_sleep_goal(day_data):
    sleep = day_data.get("sleep", 0)
    return sleep < SLEEP_GOAL

# Check if user met the water intake goal
def check_water_goal(day_data):
    water = day_data.get("water", 0)
    return water < WATER_GOAL

# Suggest tips based on what goals were missed
def suggest_tips(missed):
    tips = []
    if "sleep" in missed:
        tips.append("💤 Try sleeping 30 minutes earlier.")
    if "water" in missed:
        tips.append("💧 Don’t forget to drink enough water!")
    return tips

# Display warnings for missed health goals with suggestions
def show_warnings(data_dict):
    print("\n⚠️ Health Warnings:")
    found = False  # To check if any warning is issued
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
# Saves a dictionary of logs to a text file
def save_log_to_file(data, filename):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")

# Loads a file's data into a dictionary
def load_log_from_file(filename):
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                if ":" in line:
                    parts = line.strip().split(":", 1)
                    key = parts[0]
                    value = parts[1]
                    # Convert appropriate values to float/int
                    if key in ["water", "calories", "sleep"]:
                        data[key] = float(value)
                    elif key == "duration":
                        data[key] = int(float(value))
                    else:
                        data[key] = value
    return data

# Placeholder for daily total calculations (function used in menu)
def calculate_daily_totals(data):
    print("\n--- Daily Summary ---")
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

# Main menu function for user interaction
def main_menu():
    # Prompt user for name and day
    username = input("Enter your username: ").strip()
    if username == "":
        print("Please enter a valid username.")
        return

    print(f"\nWelcome, {username}!")
    day_number = input("Enter the day number: ").strip()
    filename = f"day{day_number}.txt"

    # Load data from file if exists, otherwise start new
    data = load_log_from_file(filename)
    data["username"] = username
    data["day"] = day_number

    # Display menu until user exits
    while True:
        print("\n===== Health Tracker Menu =====")
        print("1. Log Water")
        print("2. Log Meal/Calories")
        print("3. Log Sleep")
        print("4. Log Exercise")
        print("5. Show Daily Summary")
        print("6. Save and Exit")
        print("7. Weekly Summary (view each file)")
        print("8. Show Warnings")
        print("9. Show Weekly Stats")

        choice = input("Choose an option: ")

        # Handle user's menu choice
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
            for f in os.listdir():
                if f.startswith("day") and f.endswith(".txt"):
                    print(f"\n{f}:")
                    with open(f, "r") as file:
                        print(file.read())
        elif choice == "8":
            all_data = {}
            for f in os.listdir():
                if f.startswith("day") and f.endswith(".txt"):
                    all_data[f] = load_log_from_file(f)
            show_warnings(all_data)
        elif choice == "9":
            calculate_weekly_stats()
        else:
            print("Invalid option. Try again.")

# Run the menu if the script is executed directly
if __name__ == "__main__":
    main_menu()
