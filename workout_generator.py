import random
import sys
from easygui import *

difficulty = ["(light cuz ur soft)", "(heavy bcuz we love it)"]
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

def display_workout():
    print(selected_workout)
    print(selected_day[0])

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

    while 1:
        msgbox("Hello, world!")

        msg = "What is your favorite flavor?"
        title = "Ice Cream Survey"
        choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
        choice = choicebox(msg, title, choices)

        # note that we convert choice to string, in case
        # the user cancelled the choice, and we got None.
        msgbox("You chose: " + str(choice), "Survey Result")

        msg = "Do you want to continue?"
        title = "Please Confirm"
        if ccbox(msg, title):  # show a Continue/Cancel dialog
            pass  # user chose Continue
        else:
            sys.exit(0)  # user chose Cancel

