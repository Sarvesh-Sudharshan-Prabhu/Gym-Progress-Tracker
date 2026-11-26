import csv
import os
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
            save_workout(workout)
            print("Workout logged:", workout)

        elif choice == "2":
            print("View workout history")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def save_workout(workout):
    filename = "workouts.csv"
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["date", "exercise", "weight", "sets", "reps"]
        )

        # Prevent duplicate headers when saving additional workouts.
        if not file_exists:
            writer.writeheader()

        writer.writerow(workout)

def log_workout():
    exercise = input("Enter exercise name: ")
    weight = float(input("Enter weight in lbs: "))
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of reps: "))

    workout = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "exercise": exercise,
    "weight": weight,
    "sets": sets,
    "reps": reps
}

    return workout

if __name__ == "__main__":
    main()