import csv
import os
import math
from datetime import datetime

def display_interface():
    print("Gym Progress Tracker")
    print("1. Add a new workout")
    print("2. View workout history")
    print("3. Exit")

def main():
    while (True):
        display_interface()
        choice = input("Enter your choice: ")
        if (choice == "1"):
            workout = log_workout()
            if save_workout(workout):
                print("Workout logged:", workout)

        elif choice == "2":
            view_workout_history()

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def save_workout(workout):
    filename = "workouts.csv"

    try:
        file_exists = os.path.exists(filename)
        file_empty = not file_exists or os.path.getsize(filename) == 0

        with open(filename, "a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "exercise", "weight", "sets", "reps"]
            )

            # Prevent duplicate headers when saving additional workouts.
            if file_empty:
                writer.writeheader()

            writer.writerow(workout)

        return True

    except OSError:
        print("Unable to save workout.")
        return False

def log_workout():
    while True:
        exercise = input("Enter exercise name: ").strip()

        if exercise:
            break

        print("Exercise name cannot be empty.")

    while True:
        try:
            weight = float(input("Enter weight in lbs: "))

            if math.isfinite(weight) and weight >= 0:
                break

            print("Weight must be a non-negative finite number.")

        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            sets = int(input("Enter number of sets: "))

            if sets > 0:
                break

            print("Sets must be greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")

    while True:
        try:
            reps = int(input("Enter number of reps: "))

            if reps > 0:
                break

            print("Reps must be greater than zero.")

        except ValueError:
            print("Please enter a valid whole number.")

    workout = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "exercise": exercise,
    "weight": weight,
    "sets": sets,
    "reps": reps
}

    return workout

def view_workout_history():
    filename = "workouts.csv"

    # Prevent an error if no workouts have been recorded yet.
    if not os.path.exists(filename):
        print("No workouts recorded yet.")
        return

    try:
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            workouts = list(reader)

            if not workouts:
                print("No workouts recorded yet.")
                return

            print("\n===== Workout History =====")

            for workout in workouts:
                print("Date:", workout["date"])
                print("Exercise:", workout["exercise"])
                print("Weight:", workout["weight"], "lbs")
                print("Sets:", workout["sets"])
                print("Reps:", workout["reps"])
                print("---------------------------")

    except (OSError, csv.Error, KeyError):
        print("Unable to read workout history.")

if __name__ == "__main__":
    main()