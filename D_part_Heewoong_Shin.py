
def main_menu():
    filename = "health_log.json"
    data = load_log_from_file(filename)

    while True:
        print("\n Smart Health Tracker Menu")
        print("1. Log Meal")
        print("2. Log Sleep")
        print("3. Log Water Intake")
        print("4. Log Exercise")
        print("5. View Weekly Summary")
        print("6. View Health Alerts")
        print("7. Save and Exit")
        print("8. Exit Without Saving")

        choice = input("Select an option: ")

        if choice == "1":
            log_meal(data)
        elif choice == "2":
            log_sleep(data)
        elif choice == "3":
            log_water(data)
        elif choice == "4":
            log_exercise(data)
        elif choice == "5":
            generate_weekly_summary(data)
        elif choice == "6":
            show_warnings(data)
        elif choice == "7":
            save_log_to_file(data, filename)
            print("Exiting... Have a healthy day! 🫶")
            break
        elif choice == "8":
            print("Exiting without saving.")
            break
        else:
            print("Invalid selection. Please try again.")


# The following functions are placeholders I used while writing the menu.
#
# - log_meal(data)
# - log_sleep(data)
# - log_water(data)
# - log_exercise(data)
# - generate_weekly_summary(data)
# - show_warnings(data)
# - load_log_from_file(filename)
# - save_log_to_file(data, filename)
#
# Once your functions are finalized, I’ll replace my placeholders to match.
