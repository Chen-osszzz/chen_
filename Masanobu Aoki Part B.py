#Take the text file day1 through day7 and store them into a dictionary with the corresponding key
def load_log_from_file(filename_day1, filename_day2, filename_day3, filename_day4, filename_day5, filename_day6, filename_day7):
  #Create keys and empty lists that goes with the key
  log_data = {
        "Day": [],
        "Calories": [],
        "Sleep": [],
        "Water": [],
        "Exercise": [],
        "Exercise duration": []
    }
  filenames = [filename_day1, filename_day2, filename_day3, filename_day4, filename_day5, filename_day6, filename_day7]
  for files in filenames:
      file = open(files, "r")
      data_lines = file.readlines()
      file.close()
      for line in data_lines:
          line=line.strip()
          if line[:4] == "Day:":
              log_data["Day"].append(line[4:])
          elif line[:8] == "Calories":
              log_data["Calories"].append(line[9:])
          elif line[:5] == "Sleep":
              log_data["Sleep"].append(line[6:])
          elif line[:5] == "Water":
              log_data["Water"].append(line[6:])
          elif line[:9] == "Exercise:":
              log_data["Exercise"].append(line[9:])
          elif line[:18] == "Exercise duration:":
              log_data["Exercise duration"].append(line[18:])
  return log_data
#Calculate for calories statisitics
def calories_stat(log_data):
  count_days=len(log_data["Day"])
  calories_num_list=[]
  for i in log_data["Calories"]:
      calories_num=int(i)
      calories_num_list.append(calories_num)
  total_calories=0
  for j in calories_num_list:
      total_calories+=j
  avg_calories=total_calories/count_days
  return total_calories, avg_calories
#Calculate for sleep statistics
def sleep_stat(log_data):
      count_days=len(log_data["Day"])
      sleep_num_list=[]
      for sleep in log_data["Sleep"]:
          sleep_num=float(sleep)
          sleep_num_list.append(sleep_num)
      total_sleep=0
      for k in sleep_num_list:
          total_sleep+=k
      avg_sleep=total_sleep/count_days
      return total_sleep, avg_sleep
#Calculate water intake statistics
def water_stat(log_data):
  count_days=len(log_data["Day"])
  water_num_list=[]
  for w in log_data["Water"]:
      water_num=float(w)
      water_num_list.append(water_num)
  total_water=0
  for i in water_num_list:
      total_water+=i
  avg_water=total_water/count_days
  return total_water, avg_water
#Creates a list of different types of exercise that the user did
def exercise_type(log_data):
  exercise_list=log_data["Exercise"]
  exercise_type_list=[]
  for i in exercise_list:
      if i not in exercise_type_list:
        exercise_type_list.append(i)
  return exercise_type_list
  
#Calculate duration of the exercise statistics
def exercise_duration_stat(log_data):
  count_days=len(log_data["Day"])
  exercise_duration_num_list=[]
  for i in log_data["Exercise duration"]:
      exercise_duration_num=int(i)
      exercise_duration_num_list.append(exercise_duration_num)
  total_exercise_duration=0
  for j in exercise_duration_num_list:
      total_exercise_duration+=j
  avg_exercise_duration=total_exercise_duration/count_days
  return total_exercise_duration, avg_exercise_duration

#Calling all the function above and returning all calculated values
def weekly_summary(log_data):
  total_calories, avg_calories=calories_stat(log_data)
  total_sleep, avg_sleep=sleep_stat(log_data)
  total_water, avg_water=water_stat(log_data)
  types_of_exercise=exercise_type(log_data)
  total_exercise_duration, avg_exercise_duration=exercise_duration_stat(log_data)
  return total_calories, avg_calories, total_sleep, avg_sleep, total_water, avg_water, types_of_exercise, total_exercise_duration, avg_exercise_duration
    
#The code below is a suggestion for calling all the functions above nd return all the statistics 
#print(weekly_summary(load_log_from_file("day1.txt", "day2.txt", "day3.txt", "day4.txt", "day5.txt", "day6.txt", "day7.txt")))
