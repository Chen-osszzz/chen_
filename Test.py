import os

# ================== A. DAILY LOGGING MODULE ==================
def log_meal(data):
    food = input("What did you eat today? ")
    calories = input("How many calories did you consume? ")
    data["meal"] = food
    data["calories"] = float(calories)

def log_sleep(data):
    sleep = input("How many hours did you sleep? ")
    data["sleep"] = float(sleep)

def log_water(data):
    water = input("How much water did you drink (in liters)? ")
    data["water"] = float(water)

def log_exercise(data):
    activity = input("What exercise did you do? ")
    duration = input("How long (in minutes)? ")
    data["exercise"] = activity
    data["duration"] = int(duration)

# ================== B. SUMMARY & STATS MODULE ==================
def calculate_daily_totals(data):
    print("\n--- Daily Totals ---")
    print(f"Water: {data.get('water', 0)} L")
    print(f"Calories: {data.get('calories', 0)} kcal")
    print(f"Sleep: {data.get('sleep', 0)} hrs")
    print(f"Exercise: {data.get('exercise', 'None')} for {data.get('duration', 0)} mins")

def generate_weekly_summary():
    print("\n--- Weekly Summary ---")
    for filename in os.listdir():
        if filename.startswith("day") and filename.endswith(".txt"):
            print(f"\n{filename}:")
            with open(filename, "r") as f:
                print(f.read())

# ================== C. ALERTS & GOALS MODULE ==================
SLEEP_GOAL = 7.0
WATER_GOAL = 2.0

def check_sleep_goal(day_data):
    sleep = day_data.get("sleep", 0)
    return sleep < SLEEP_GOAL

def check_water_goal(day_data):
    water = day_data.get("water", 0)
    return water < WATER_GOAL

def suggest_tips(missed):
    tips = []
    if "sleep" in missed:
        tips.append("💤 Try sleeping 30 minutes earlier.")
    if "water" in missed:
        tips.append("💧 Don’t forget to drink enough water!")
    return tips

def show_warnings(data_dict):
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
def save_log_to_file(data, filename):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")

def load_log_from_file(filename):
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
        print("\n===== Health Tracker Menu =====")
        print("1. Log Water")
        print("2. Log Meal/Calories")
        print("3. Log Sleep")
        print("4. Log Exercise")
        print("5. Show Daily Summary")
        print("6. Save and Exit")
        print("7. Weekly Summary")
        print("8. Show Warnings")

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
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
