# C-Alerts and Goals Module-Chen

SLEEP_GOAL = 7.0  # set standard hours
WATER_GOAL = 2.0  # set standard liters


#check sleep goal
def check_sleep_goal(day_data):
    if "sleep" in day_data:
        sleep = day_data["sleep"]
    else:
        sleep = 0
    return sleep < SLEEP_GOAL

# check water goal
def check_water_goal(day_data):
    if "water" in day_data:
        water = day_data["water"]
    else:
        water = 0
    return water < WATER_GOAL

# according to the goal, give suggestion
def suggest_tips(missed):
    tips = []
    if "sleep" in missed:
        tips.append("💤 try to sleep early,maybe 30 mins before")
    if "water" in missed:
        tips.append("💧 remember to drink more water")
    return tips

# show all the notifications 
def show_warnings(data):
    print("\n health warning：")

    found = False  #weather it has warning or not

    for date, day in data.items():
        missed = []
        if check_sleep_goal(day):
            missed.append("sleep")
        if check_water_goal(day):
            missed.append("water")

        if missed:
            found = True
            print(f"\n📅 date：{date}")
            if "sleep" in missed:
                if "sleep" in day:
                    print(f"  ! not enough sleep：{day['sleep']} hours（goal：{SLEEP_GOAL}）")
                else:
                    print(f"  ! no sleep data recoring（goal：{SLEEP_GOAL} hours）")
            if "water" in missed:
                if "water" in day:
                    print(f"  !do not drink enough water：{day['water']} liters（goal：{WATER_GOAL}）")
                else:
                    print(f"  ! no water data recording（goal：{WATER_GOAL} liters）")

            for tip in suggest_tips(missed):
                print("  suggest：", tip)

    if not found:
        print(" Congrs! All you achieved all your goals!!\n")
