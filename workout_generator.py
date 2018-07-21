import random
import sys
from easygui import *

difficulty = ["(light reps cuz ur soft)", "(heavy reps bcuz we love it)"]
days = ["Chest/Tris", "Back/Bis", "Leg", "Shoulder"]

incline_press = ["Incline Dumbbell Press", "Incline Barbell Press"]
flat_press = ["Flat Dumbbell Press", "Flat Barbell Press", "Decline Barbell Press"]
tricep_up = ["Cable Overhead Extension", "Skullcrushers", "Close-Grip Bench"]
tricep_down = ["Dips", "Cable Tricep Pushdown"]
chest_misc = ["Seated Machine Chest Press", "Seated Machine Fly", "Incline Dumbbell Pull-Over"]

row = ["Seated Row", "Bent-Over Barbell Row", "One Arm Dumbbell Row"]
lat_pull = ["Lat Pulldown", "Pull Up", "Close-Grip Pulldown"]
bicep_pull = ["Chin Up", "Reverse-Grip Bent-Over Row"]
bicep_curl = ["Barbell Curl", "Incline Dumbbell Curl", "Standing Dumbbell Curl"]

squat = ["Barbell Squat", "Hack Squat", "Leg Press"]
deadlift = ["Barbell Deadlift", "Romanian Deadlift"]
lunge = ["Dumbbell Lunges", "Dumbbell Rear Lunges", "Dumbbell Step Ups", "Barbell Lunges"]
leg_curl = ["Lying Leg Curls", "Seated Leg Curls"]
calf_raise = ["Sitting Calf Raises", "Standing Barbell Calf Raises", "Standing Calf Raises"]
leg_misc = ["Leg Extensions", "Thigh Abductors"]

shoulder_press = ["Seated Barbell Military Press", "Arnold Dumbbell Press", "Seated Dumbbell Press"]
lateral_raise = ["Dumbbell Side Lateral Raise", "Machine Lateral Raise"]
rear_delts = ["Machine Reverse Fly", "Seated Bent-Over Rear Delt Raise", "Face Pull"]
front_raise = ["Incline Dumbbell Front Raise", "Standing Dumbbell Front Raise"]
trap = ["Dumbbell Shrugs", "Upright Rows"]

chest_tris = [incline_press, flat_press, tricep_up, tricep_down, chest_misc]
back_bis = [row, lat_pull, bicep_pull, bicep_curl]
legs = [squat, deadlift, lunge, leg_curl, calf_raise, leg_misc]
shoulders = [shoulder_press, lateral_raise, rear_delts, front_raise, trap]

workouts = [chest_tris, back_bis, legs, shoulders]
selected_workout = []
selected_day = []

def create_workout_str():
    workout_str = "It's " + str(selected_day[0]) + " Day bitch!!!!\n\n"
    for exercise in selected_workout:
        workout_str += exercise[0] + ", " + exercise[1] + "\n"
    return workout_str

def display_workout():
    workout_str = create_workout_str()

    first_image = "fattymatty.gif"
    msgbox("It's da boiiiiiiiiiii!!!!!!!!!!!!!!!!!!!", image=first_image)

    msg = "u sure u wanna workout today?"
    title = "don't be soft"
    choices = ["Yes", "Fuck Yes"]
    choicebox(msg, title, choices)

    second_image = "buffmatty.gif"
    msgbox(workout_str)
    msgbox("MattyIce is bout to be lookin' MattyNice ;)", image=second_image)
    print(workout_str)

def select_workout():
    day_seed = random.randint(0, len(workouts) - 1)
    selected_day.append(days[day_seed])
    for exercise in workouts[day_seed]:
        set_seed = random.randint(0, len(exercise) - 1)
        rep_seed = random.randint(0, len(difficulty) - 1)
        workout = exercise[set_seed]
        reps = difficulty[rep_seed]
        selected_workout.append((workout, reps))

if __name__ == "__main__":
    select_workout()
    display_workout()


