import random

incline_press = ["Incline Dumbbell Press", "Incline Barbell Press"]
flat_press = ["Flat Dumbbell Press", "Flat Barbell Press", "Decline Barbell Press"]
tricep_up = ["Cable Overhead Extension", "Skullcrushers", "Close-Grip Bench"]
tricep_down = ["Dips", "Cable Tricep Pushdown"]
chest_misc = ["Seated Machine Chest Press", "Seated Machine Fly", "Incline Dumbbell Pull-Over"]

chest = [incline_press, flat_press, tricep_up, tricep_down, chest_misc]

workouts = [chest]

selected_workout = []

def select_chest():
    for exercise in chest:
        seed = random.randint(0, len(exercise) - 1)
        selected_workout.append(exercise[seed])

def display_workout():
    print(selected_workout)

def select_workout(seed):
    workout = {
        1: select_chest
    }
    workout[seed]()

if __name__ == "__main__":
    seed = random.randint(1, len(workouts))
    select_workout(seed)
    display_workout()

