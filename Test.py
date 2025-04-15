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
#Function for calculating and displaying the weekly stats
def calculate_weekly_stats():
    #Set values for update as files get saved
    print("\n--- Weekly Statistics ---")
    total_water = 0
    total_calories = 0
    total_sleep = 0
    total_exercise_duration = 0
    count = 0
    #Loop through all the files in the current directory. 
    for filename in os.listdir():
        #Reads the files the starts with "day" and endswith ".txt".
        if filename.startswith("day") and filename.endswith(".txt"):
            #With function ensures it opens and closes after reading the file
            with open(filename, "r") as file:
                #Reads each line in the txt files
                for line in file:
                    if ":" in line:
                        #Splits the string in the txt file with the colon and sets key and values
                        key, value = line.strip().split(":", 1)
                        if key == "water":
                            total_water += float(value)
                        elif key == "calories":
                            total_calories += float(value)
                        elif key == "sleep":
                            total_sleep += float(value)
                        elif key == "duration":
                            total_exercise_duration += int(float(value))
                count += 1

    if count == 0:
        print("No data found for the week.")
        return
    #Calculates the average of each values, round them into two decimal places and dispaly
    print(f"Average Water: {round(total_water / count, 2)} L")
    print(f"Average Calories: {round(total_calories / count, 2)} kcal")
    print(f"Average Sleep: {round(total_sleep / count, 2)} hrs")
    print(f"Average Exercise Duration: {round(total_exercise_duration / count, 2)} mins")

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
#Coded by part A coder but relocated for better clarity to call the functions
#Writes the user inputs from part A into a txt file 
def save_log_to_file(data, filename):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}:{value}\n")
#Coded by part B coder but relocated for better clarity to call the functions
#Reads the txt files and set a dictionary with values of list 
def load_log_from_file(filename):
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                if ":" in line:
                    parts = line.strip().split(":", 1)
                    key = parts[0]
                    value = parts[1]
                    if key in ["water", "calories", "sleep"]:
                        data[key] = float(value)
                    elif key == "duration":
                        data[key] = int(float(value))
                    else:
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
        print("7. Weekly Summary (view each file)")
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

if __name__ == "__main__":
    main_menu()
